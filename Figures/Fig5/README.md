This repository holds the parameters and instructions for 'Fig5: Anonymity with fixed vs variable propagation delays \tau'.
For each set (Fig5.a and Fig5.b), update ConfigFile.ini and main.py as follows: 
For Fig5.a:
    
    In ConfigFile.ini:
        type = dynamic                      # type values are 'fixed', 'dynamic' 'fixed_per_mix'
        l_mixes_per_layer = 10


    In main.py:
        mu = 1
        n_layer = arg #int(config['TOPOLOGY']['n_layers'])
        param = [1,5,10,15]
        p = Pool(processes=4, maxtasksperchild=1)


For Fig5.b:
    
    In ConfigFile.ini:
        type = dynamic                      # type values are 'fixed', 'dynamic' 'fixed_per_mix'


    In main.py:
        mu = 0.001
        n_layer = arg #int(config['TOPOLOGY']['n_layers'])
        param = [1,5,10,15]
        p = Pool(processes=4, maxtasksperchild=1)

To execute:

    run "nohup python3 main.py > results.txt &"
    Entropy values will consist of 4 arrays, each corresponds to the different number of layers configuration.
    Copy each array of entropy values in the jupyter file fig5_X.ipynb
    
    Note: For this set of experiments, we use 4 CPUs, hence the command "p = Pool(processes=4, maxtasksperchild=1)". If your computer does not allow this, you can replace "p = Pool(processes=4, maxtasksperchild=1)" by "p = Pool(processes=1, maxtasksperchild=1)" and "param = [1,5,10,15]" by "param = [1]" each time replace the value of the array param by the correct number of layers.