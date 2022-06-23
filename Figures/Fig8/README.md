This repository holds the parameters and instructions for 'Fig8:Mean entropy as a function of the mixnet width W for various b and B L=3, \lambda_U=5000, D_{e2e}=1s'.



In main.py, for each line in figure Fig8 that corresponds to a different value "b" we change the values of corrupt_mixes:

        corrupt_mixes = int(0 * total_n_mixes)                   #values are 0, 0.1
    
In main.py, for each line in figure Fig8 that corresponds to a different value "B" we change the values of corrupt_mixes:

        corrupt_mixes = 30                   #values are 9,  15, 30
    
Each time you change the value of "b" or "B", copy the array of entropy values in the jupyter file fig8.ipynb