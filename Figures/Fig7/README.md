This repository holds the parameters and instructions for 'Fig7: Mean Entropy wrt number of layers $L$ for various D_{e2e}, considering \lambda_U=5000 and mixnet width W=10.'.

Each figure( either Fig7.a or Fig7.b) has 5 plots, each plot corresponds to a different E2E value. We vary the number of layers in main.py in the argument param.
In main.py param values as well as p values change as follows:

1. For E2E= 5, E2E = 2, E2E=1:

        p = Pool(processes=19, maxtasksperchild=1)
        param = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

2. For E2E = 0.5, we can only compute the entropy values for up to 9 layers:

        p = Pool(processes=9, maxtasksperchild=1)
        param = [1, 2, 3, 4, 5, 6, 7, 8, 9]

3. For E2E = 0.25 we can only compute the entropy values for up to 4 layers:

        p = Pool(processes=4, maxtasksperchild=1)
        param = [1, 2, 3, 4]

Please note that in order for parallel processing where each processing corresponds to a different layer, we use a computer with more than 19 CPUs.

If you do not have access to a computer that is able to do parallel processing, first change p = Pool(processes=1, maxtasksperchild=1) then change param values to param = [1] then once the processing is done, copy the entropy value in the corresponding jupyter file then proceed to layer 2 value by changing param = [2] etc.

Instructions for Fig7.a:

In main.py

        corrupt_mixes = 0

Instructions for Fig7.b:

In main.py
        
        corrupt_mixes = int(0.1 * n_total_mixes)

    
In ConfigFile.ini for each line that corresponds to a different end-to-end latency we change the value ETE:

        E2E = 5             #values take 5, 2, 1, 0.5, 0.25