This repository holds the parameters and instructions for 'Fig6: Anonymity with uniform vs biased routing considering no adversarial nodes and 10% of adversarial nodes'.


Instructions for uniform routing:

In main.py

        p = Pool(processes=2, maxtasksperchild=1)
        param = [0, 0.1]
        corrupt_mixes = rate * total_n_mixes
    
In ConfigFile.ini:

        routing_weights = uniform
        n_layers = 3
        l_mixes_per_layer = 10

Instructions for Biased routing:

In main.py

        p = Pool(processes=2, maxtasksperchild=1)
        param = [0, 0.1]
        corrupt_mixes = rate * total_n_mixes
    
In ConfigFile.ini:

        routing_weights = biased
   

Note:   Entropy values will consist of 2 arrays, each corresponds to the different corruption rate. Copy each array of entropy values in the jupyter file fig6.ipynb