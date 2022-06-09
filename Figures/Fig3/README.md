This subfolder holds the parameters and instructions for 'Fig3: Fraction \alpha_F for different values of L and B in a network of a hundred nodes.'

In order to be able to reproduce the data points:
    
    For each value in Figure3 we change the values of B, L accordingly
    run 'python3 HyperGeometric.py'
    
    L= 2            # L values take 2, 3 , 4, 5
    B = 10          # B values take 30, 20, 10
To replicate the graph copy the printed alpha_F in the jupyter file (alphaF_b10 for the configuration B=10, alpha_b20 for the configuration B=20 etc).