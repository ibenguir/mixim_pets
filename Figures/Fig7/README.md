This repository holds the parameters and instructions for 'Fig7: Mean Entropy wrt number of layers $L$ for various D_{e2e}, considering \lambda_U=5000 and mixnet width W=10.'.


Instructions for Fig7.a:

In main.py

        p = Pool(processes=19, maxtasksperchild=1)
        param = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        corrupt_mixes = 0
        n_layer = rate
    
In ConfigFile.ini for each line that corresponds to a different end-to-end latency we change the value ETE:

        ETE = 5
        l_mixes_per_layer = 10

Instructions for Fig7.b:

In main.py

        p = Pool(processes=19, maxtasksperchild=1)
        param = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        corrupt_mixes = 0.1 * n_total_mixes
        n_layer = rate
    
