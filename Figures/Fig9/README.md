This repository holds the parameters and instructions for 'Fig9:Average anonymity in low-traffic conditions (\lambda_U=100 m/s) with link-based and partial-route dummy strategies towards network adversaries corrupting b=0 and b=0.1 of a mixnet with L=3, W=50, and D_{e2e}=1s.'


In main.py, for each line that corresponds to a different b we change the values of corrupt_mixes:

        rate_mix_dummies = rate
        corrupt_mixes = int(0 * n_total_mixes)                #values are 0, 0.1
        
        p = Pool(processes=4, maxtasksperchild=1)
        param = [0, 1.5*100, 1.5*1000, 1.5*10000]
In ConfigFile.ini:
        
        n_clients= 100
        lambda_c = 1
        ETE = 1
        n_layer = 3
        l_mixes_per_layer = 50
        link_based_dummies = False          #True for the partial route
        multiple_hop_dummies = False        #True for the second set of experiments

