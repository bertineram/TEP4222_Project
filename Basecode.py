# Authors: Andrine Roska Vallestad, Ida Bertine Rambøl, Kristian L. Karstensen
# something 
# something 
# header stuff
#Tester her 123
#ikke godkjenn
#%%
# Import packages
import pandas as pd
import numpy as np
import matplotlib as plt


#%%
# Import data

    # Note:  a bit unsure aboute header and index_col, need to double check
Y = pd.read_csv(r"Data/Y.txt", sep='\t', header=[0,1], index_col=[0,1])
Z = pd.read_csv(r"Data/Z.txt", sep='\t', header=[0,1], index_col=[0,1])
F = pd.read_csv(r"Data/F.txt", sep='\t', header=[0,1], index_col=[0,1])

    # Same note hear, header and index_col
unit_F = pd.read_csv(r"Data/unit_F.txt", sep='\t', header=0, index_col=[0,1])
unit_Z = pd.read_csv(r"Data/unit_Z.txt", sep='\t', header=0, index_col=[0,1])

#%%
display(unit_F)

#%%

# What do we do with the json files?
    # file_parameters.json
    # metadata.json
