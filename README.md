This repository holds the code and data for our PETS'22 paper titled 'Parameters Optmization'.



The reproducibility steps described in this repository require a number of installed packages. Installation and setup of those will depend on your system. In case you are running a recent Ubuntu, we recommend to run the following steps so that the commands we list in the READMEs across this repository complete successfully:

    Update your package list: sudo apt update
    Install Python 3 (programming language): sudo apt install python3,
    Install Pip (Python package manager): sudo apt install python3-pip,
    Install Jupyter Lab and Python libraries simpy, numpy, pandas, and matplotlib: pip install simpy jupyterlab numpy pandas seaborn matplotlib,

The main function of the simulator is entropy computation (details are provided in Section3.2):

![](/home/iness/Desktop/entropy.png)

Instructions for Reproduction: In order to reproduce the graphs of Fig5, Fig6, Fig7, Fig8 and Fig9, there are 3 steps: (1) Initialize the parameters in ConfigFile.ini (2) run the main function (3) plot the result. 

For each graph:    
    
    Update the ConfigFile.ini according to the parameters provided in README.md under Figures/ 
    run 'nohup python3 main.py &'
    When the simulation time is reached, result will be '/Logs/Entropy.csv'
