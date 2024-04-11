# Authors: Andrine Roska Vallestad, Ida Bertine Rambøl, Kristian L. Karstensen
# Mail:
# Version stuff
# something 
# header stuff
#Tester her 123


#%%
# Import packages
import pandas as pd
import numpy as np
import matplotlib as plt


#%%
# Import Eurostat Urbanization data

 ## Make a simplified excel for this !!!

Eurostat =  pd.read_excel(r"Data/Eurostat_Urb.xlsx", header=[0,1]).fillna(0)
Eurostat

#%%
# Import calculated CBi for Energy Footprint in Norwegian households
CBi = pd.read_csv(r"CBi_NOR_test.csv", header=[0], index_col=[0,1])
CBi

#%%
# Import product and classification category
Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1]).fillna(0)
Category


#%%


