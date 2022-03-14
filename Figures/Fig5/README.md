This repository holds the parameters and instructions for 'Fig5: Anonymity with fixed vs variable propagation delays \tau'.
For each set (Fig5.a and Fig5.b), update ConfigFile.ini and main.py as follows: 
For Fig5.a:
    
    In ConfigFile.ini:
        n_clients= 500
        lambda_c = 10
        l_mixes_per_layer = 10
        type = dynamic                      # type values are 'fixed', 'dynamic' 'fixed_per_mix'


    In main.py:
        n_layer = rate
        mu = 1
        p = Pool(processes=4, maxtasksperchild=1)
        param = [1, 5, 10, 15]

For Fig5.b:
    
    In ConfigFile.ini:
        n_clients= 500
        lambda_c = 10
        l_mixes_per_layer = 10
        type = dynamic                      # type values are 'fixed', 'dynamic' 'fixed_per_mix'


    In main.py:
        n_layer = rate
        mu = 0.001
        p = Pool(processes=4, maxtasksperchild=1)
        param = [1, 5, 10, 15]
After updating the files:

    run "nohup python3 main.py > result.txt &"
    copy each array of entropy values in the jupyter file fig5_a.ipynb