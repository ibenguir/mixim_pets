This repository holds the code and data for our PETS'22 paper titled 'Parameters Optmization'.



The reproducibility steps described in this repository require a number of installed packages. Installation and setup of those will depend on your system. In case you are running a recent Ubuntu, we recommend to run the following steps so that the commands we list in the READMEs across this repository complete successfully:

    Update your package list: sudo apt update
    Install Python 3 (programming language): sudo apt install python3,
    Install Pip (Python package manager): sudo apt install python3-pip,
    Install Jupyter Lab and Python libraries simpy, numpy, pandas, and matplotlib: pip install simpy jupyterlab numpy pandas seaborn matplotlib,

The main function of the simulator is entropy computation (details are provided in Section3.2):

![](/home/iness/Desktop/entropy.png)

All the scripts of the simulator are under the main folder Scripts. After installing the above packages:
 
    run 'python3 main.py`

Please note that simulation might take time, so we usually run the following command:
        
    `nohup python3 main.py > result.txt &`
When simulation is done (we can simply check by using the command `'top'`) results, entropy data, is printed in the file text result.txt.
       
    tail -1 result.txt


We log different types of data (number of message, average latency etc) and are all stored in the file 'result.txt'. We can check all data using:

    nano result.txt

Instructions for Reproduction the exact graphs in the paper:
    In order to reproduce the graphs of Fig5, Fig6, Fig7, Fig8 and Fig9, there are 3 steps: (1) Initialize the parameters in ConfigFile.ini (2) run the main function (3) plot the result. 

For each graph:
    
    read README.md under each subfolder
    Update the content of the files ConfigFile.ini and main.py by the files uder Figures/FigX 
    run 'nohup python3 main.py > result.txt &'
    When the simulation time is reached, result will be in result.txt

Note that the instructions in main.py for certain configurations require more than just one CPU. However, using more than one CPU is only for speed puposes.
One can simply always use one CPU for each simulation, save the result,  and update the next parameter etc.


All the changes in each configuration happen in ConfigFile or main.py. For this reason we have included under each subfolder, these files with the corresponding parameters. One can simply replace main.py and ConfigFile.ini under the main Scripts folder.