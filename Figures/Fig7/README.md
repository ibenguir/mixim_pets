This repository holds the parameters and instructions for 'Fig7: Mean Entropy wrt number of layers $L$ for various D_{e2e}, considering \lambda_U=5000 and mixnet width W=10.'.


Instructions for Fig7.a:

In main.py

        corrupt_mixes = 0

Instructions for Fig7.b:

In main.py
        
        corrupt_mixes = int(0.1 * n_total_mixes)

    
In ConfigFile.ini for each line that corresponds to a different end-to-end latency we change the value ETE:

        ETE = 5             #values take 5, 2, 1, 0.5, 0.25