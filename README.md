This repository holds the code and data for our PETS'22 paper titled 'Parameters Optmization'.



The reproducibility steps described in this repository require a number of installed packages. Installation and setup of those will depend on your system. In case you are running a recent Ubuntu, we recommend to run the following steps so that the commands we list in the READMEs across this repository complete successfully:

    Update your package list: sudo apt update
    Install Python 3 (programming language): sudo apt install python3,
    Install Pip (Python package manager): sudo apt install python3-pip,
    Install Jupyter Lab and Python libraries simpy, numpy, pandas, seaborn, and matplotlib: pip install simpy jupyterlab numpy pandas seaborn matplotlib,

Instructions for Reproduction:

    First, you need to chose the parameters for each scenario
    All the parameters of the network are in the file ConfigFile.ini
    
    The main function of this programme is main.py
    run 'nohup python3 main.py &'
    When the simulation time is reached, result will be '/Logs/entropy.csv'
