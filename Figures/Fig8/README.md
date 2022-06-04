This repository holds the parameters and instructions for 'Fig8:Mean entropy as a function of the mixnet width W for various b and B L=3, \lambda_U=5000, D_{e2e}=1s'.



In main.py, for each line that corresponds to a different b we change the values of corrupt_mixes:

        corrupt_mixes = int(0 * total_n_mixes)                   #values are 0, 0.1
    
