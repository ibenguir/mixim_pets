This repository holds the parameters and instructions for 'Fig8:Mean entropy as a function of the mixnet width W for various b and B L=3, \lambda_U=5000, D_{e2e}=1s'.



In main.py, for each line that corresponds to a different b we change the values of corrupt_mixes:

        p = Pool(processes=10, maxtasksperchild=1)
        param = [10,20,30,40,50,60,70,80,90,100]
        corrupt_mixes = 0 * n_total_mixes                   #values are 0, 0.1
    
In ConfigFile.ini for each line that corresponds to a different B we change the value corrupt_mixes:

        ETE = 1
        n_layer = 3
        corrupt_mixes = 0                                   #values are 0, 9,15,30

