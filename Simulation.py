import simpy
import Client
from Network import Network
import pandas as pd
import numpy as np
from Relay import Attacker
from Log import Log

DEFAULT_TOPOLOGY = 'stratified'
logDir = 'Logs/'


class Simulation(object):

    def __init__(self, mix_type, simDuration, rate_client, mu, logging, topology, fully_connected, n_clients,
                 flush_percent, printing, routing, n_layers,
                 n_mixes_per_layer, corrupt, unifrom_corruption, probability_dist_mixes, client_dummies,
                 rate_client_dummies, link_based_dummies, multiple_hops_dummies, rate_mix_dummies, Network_template):

        self.Log = Log()
        self.logs = []
        self.logging = logging
        self.printing = printing
        self.topology = topology
        self.fully_connected = fully_connected
        self.flush_percent = flush_percent

        self.client_dummies = client_dummies
        self.rate_client_dummies = rate_client_dummies
        self.link_based_dummies = link_based_dummies
        self.multiple_hop_dummies = multiple_hops_dummies
        self.rate_mix_dummies = rate_mix_dummies

        self.n_clients = n_clients
        self.clientsSet = set()
        self.rate_client = rate_client  # average delay between messages being sent from client
        self.mu = mu  # average delay at poisson mixes
        self.n_layers = n_layers
        self.n_mixes_per_layer = n_mixes_per_layer
        self.corrupt = corrupt
        self.probability_dist_mixes = probability_dist_mixes
        self.unifrom_corruption = unifrom_corruption
        self.mix_type = mix_type
        self.routing = routing
        self.env = simpy.Environment()
        self.SimDuration = simDuration
        self.burnout = 10
        self.n_targets = 0
        self.MsgsDropped = []

        self.dummyID = 0
        time_stable = ((1 / self.rate_client) / self.n_layers) * self.mu + 2
        self.n_targets = int(((self.SimDuration - time_stable)) / 2)

        self.network = Network(self.mix_type, self.n_layers, self.n_mixes_per_layer, self.corrupt,
                               self.unifrom_corruption,
                               self.flush_percent, self.topology, fully_connected,
                               self.probability_dist_mixes, self.link_based_dummies, self.multiple_hop_dummies,
                               self.rate_mix_dummies,
                               Network_template, self.n_targets)

        self.set_clients(self.probability_dist_mixes, self.n_targets, self.client_dummies, self.rate_client_dummies,
                         self.Log)
        # self.stableMix = [False for i in range(self.n_mixes_per_layer*self.n_layers)]  # only start attack after mixes are stable
        self.stableChains = [False for i in range(1, 1 + 6)]  # only start attack after chains are stable
        self.stableMixL1 = [False for i in range(self.n_mixes_per_layer)]  # only start attack after mixes are stable
        self.attacker = Attacker(self, self.n_targets)  # attacker/relay object
        self.endEvent = self.env.event()  # event that triggers the end of the simulation
        self.TargetMessageEnd = False  # if target message has reached the end client
        self.startAttack = False  # if the attacker is allowed to choose a target message
        self.NumberMsgsDropped = 0
        self.numberrounds = []

    def set_stable_mix(self, index):
        self.stableMixL1[index] = True
        if all(self.stableMixL1):
            yield self.env.timeout(2)
            self.startAttack = True

    def set_stable_chain(self, position):
        if self.mix_type == 'pool':
            yield self.env.timeout(10)
            self.startAttack = True
        self.stableChains[position - 1] = True
        if all(self.stableChains):
            yield self.env.timeout(2)
            self.startAttack = True

    def set_clients(self, probabilityDistribution, n_targets, client_dummies, rate_client_dummies, Log):
        if self.topology == 'stratified':
            for client_no in range(self.n_clients):
                client = Client.Client(self, client_no, self.network.network_dict, self.rate_client, self.mu,
                                       probabilityDistribution, n_targets, client_dummies, rate_client_dummies, Log)
                self.clientsSet.add(client)
            for client in self.clientsSet:
                client.other_clients = self.clientsSet - {client}

    def run(self, time=None):
        # Print statements and results from here
        if self.printing:
            print('\n')
            print('----------Simulation Data----------')
            print('Topology: {}'.format(self.topology))
            print('Routing strategy: {}'.format(self.routing))
            print('Mix type: {}'.format(self.mix_type))
            print('Layers: {}, amount of mixes per layer: {}'.format(self.n_layers, self.n_mixes_per_layer))
            print(
                'Amount of clients: {}, average delay between 2 messages: {}'.format(self.n_clients, self.rate_client))
            l = ''
            index = 0
            if self.topology == 'stratified':
                for layer in self.network.network_dict:
                    k = 'Layer {}: [ '.format(layer)
                    for mixnb in range(self.n_mixes_per_layer):
                        k += str(self.network.network_dict[layer][mixnb])
                        if self.network.network_dict[layer][mixnb].corrupt:
                            index += 1
                    l += k + ']'
                    l += '\n'
                print(l)
            elif self.topology == 'cascade':
                k2 = 'Cascade'
                for cascade in self.network.list_cascades:
                    for mixnb in range(3):
                        k2 += str(cascade[mixnb].id)
                    l += k2 + ']'
                    l += '\n'
            print('----------Starting Simulation----------')
        if self.printing:
            print('Topology: {}'.format(self.topology))
        if time is None:
            self.env.run(until=self.endEvent)
        else:
            self.env.run(until=time)

        if self.printing:
            print('----------Simulation Ended---------')
            print('\n')

        # Data from Clients(senders and receivers)
        df_sent_messages = pd.DataFrame(self.Log.sent_messages)
        df_received_messages = pd.DataFrame(self.Log.received_messages)
        df_dummies_messages = pd.DataFrame(self.Log.dummy_messages)

        if self.logging:
            df_sent_messages.to_csv(f'{logDir}SentMessages.csv')
            df_received_messages.to_csv(f'{logDir}ReceivedMessages.csv')
            df_dummies_messages.to_csv(f'{logDir}DummyMessages.csv')
        else:
            pass

        entropy = []
        for i in range(0, self.n_targets):
            entropy.append(0.0)
        tableProb = df_received_messages['MessageTarget'].to_numpy(copy=True)
        for j in range(0, self.n_targets):
            for m in range(len(tableProb)):
                if tableProb[m][j] != 0:
                    entropy[j] += - tableProb[m][j] * np.log2(tableProb[m][j])

        dict_entropy = {'Entropy': entropy}
        df_entropy = pd.DataFrame(dict_entropy)
        df_entropy.to_csv(f'{logDir}Entropy.csv')

        entropy_mean = np.mean(entropy)
        try:
            entropy_median = np.median(entropy)
            entropy_q25 = np.quantile(entropy, .25)
        except:
            entropy_median = 0
            entropy_q25 = 0

        sum_delays = 0
        for re, le in zip(self.Log.received_messages["MessageTimeReceived"],
                          self.Log.received_messages["MessageTimeLeft"]):
            sum_delays += (re - le)
        average_delay = sum_delays / len(self.Log.received_messages["MessageTimeReceived"])
        if self.printing:
            print('----------Simulation Stats----------')
            # print('Average Latency: {}'.format(latency))
            print("Number of targets chosen", self.n_targets)
            print('Number of Real messages generated', len(self.Log.sent_messages["MessageID"]))
            print('Number of Real messages Received', len(self.Log.received_messages["MessageID"]))
            print('Number of Dummy messages dropped', len(self.Log.dummy_messages["DummyID"]))
            print("Average delay per message", average_delay)
            print('-------------------------------------')

        return entropy, entropy_mean, entropy_median, entropy_q25