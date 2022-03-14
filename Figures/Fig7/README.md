This repository holds the parameters and instructions for 'Fig7: Mean Entropy wrt number of layers $L$ for various D_{e2e}, considering \lambda_U=5000 and mixnet width W=10.'.


Instructions for Fig7.a:

In main.py

        corrupt_mixes = 0
        n_layer = rate
        mu =(int(config['TOPOLOGY']['E2E']) - (n_layer + 1)*0.05)/n_layer

        p = Pool(processes=19, maxtasksperchild=1)
        param = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

    

Instructions for Fig7.b:

In main.py
        
        n_layer = rate
        corrupt_mixes = int(0.1 * n_total_mixes)
        mu =(int(config['TOPOLOGY']['E2E']) - (n_layer + 1)*0.05)/n_layer

        p = Pool(processes=19, maxtasksperchild=1)
        param = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    
In ConfigFile.ini for each line that corresponds to a different end-to-end latency we change the value ETE:

        ETE = 5             #values take 5, 2, 1, 0.5, 0.25
        l_mixes_per_layer = 10
        n_clients= 500
        lambda_c = 10