This repository holds the parameters and instructions for 'Fig9:Average anonymity in low-traffic conditions (\lambda_U=100 m/s) with link-based and partial-route dummy strategies towards network adversaries corrupting b=0 and b=0.1 of a mixnet with L=3, W=50, and D_{e2e}=1s.'


1. For Partial Route:

    In main.py:

        corrupt_mixes = int(0 * total_n_mixes)                #values are 0, 0.1
        p = Pool(processes=4, maxtasksperchild=1)
        param = [0, 100, 1000, 10000]
        
        

   In ConfigFile.ini:

        link_based_dummies = False
        partial_route = True

2. For Link-based:

    In main.py:

           corrupt_mixes = int(0 * n_total_mixes)                #values are 0, 0.1
           p = Pool(processes=4, maxtasksperchild=1)
           param = [0, 150, 1500, 15000]
        
        
   In ConfigFile.ini:

        link_based_dummies = True
        partial_route = False
