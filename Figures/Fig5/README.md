This repository holds the parameters and instructions for 'Fig5: Anonymity with fixed vs variable propagation delays \tau'.
For each set (Fig5.a and Fig5.b), update ConfigFile.ini and main.py as follows: 
For Fig5.a:
    
    In ConfigFile.ini:
        type = dynamic                      # type values are 'fixed', 'dynamic' 'fixed_per_mix'


    In main.py:
        mu = 1

For Fig5.b:
    
    In ConfigFile.ini:
        type = dynamic                      # type values are 'fixed', 'dynamic' 'fixed_per_mix'


    In main.py:
        mu = 0.001
Copy main.py and ConfigFile.ini in the main folder Scripts:

    run "nohup python3 main.py &"
    copy each array of entropy values in the jupyter file fig5_X.ipynb