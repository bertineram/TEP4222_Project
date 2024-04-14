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
Eurostat =  pd.read_excel(r"Data/Urbanization_Eurostat.xlsx", header=[0], index_col=[0]).fillna(0)
Eurostat

#%%

Urbanization = Eurostat
Urb_sum = Urbanization.sum(axis=0)
Urb_sum


#%%
# Urbanization categories
Urb_Cat = list(set(Eurostat.columns.get_level_values(0)))
Urb_Cat

#%%
# Import calculated CBi for Energy Footprint in Norwegian households
CBi = pd.read_excel(r"CBi_NOR_test.xlsx", header=[0], index_col=[0])
CBi


#%%
# Import product and classification category
Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1])#.fillna(0)

COICOP = Category.columns.get_level_values(0)
COICOP

#%%
# Making a new DataFrame
CBi_Urb = pd.DataFrame(index=Category.columns)
CBi_Urb['CB Energy Footprint'] = 0
CBi_Urb


#%%
####################################################
#####      CBi_Urb['CB Energy Footprint']      #####


#%%
# Picking out the first COICOP category to test before for loop below
CP01 = Category.iloc[:, 0]
CP01 = CP01.dropna('index')
CP01

#%%
# For loop to make variables for each COICOP category in Eurostat
for i in range(12):
    cp_name = 'CP{:02d}'.format(i+1)
    cp_variable = Category.iloc[:, i]
    globals()[cp_name] = cp_variable.dropna('index')


#%%
# Summing up the relevant values for each COICOP category

#CBi_Urb.loc[('[CP01]', 'Food and non-alcoholic beverages')] = CBi.loc[CP01].values.sum()
CBi_Urb.iloc[0] = CBi.loc[CP01].values.sum()
CBi_Urb.iloc[1] = CBi.loc[CP02].values.sum()
CBi_Urb.iloc[2] = CBi.loc[CP03].values.sum()
CBi_Urb.iloc[3] = CBi.loc[CP04].values.sum()
CBi_Urb.iloc[4] = CBi.loc[CP05].values.sum()
CBi_Urb.iloc[5] = CBi.loc[CP06].values.sum()
CBi_Urb.iloc[6] = CBi.loc[CP07].values.sum()
CBi_Urb.iloc[7] = CBi.loc[CP08].values.sum()
CBi_Urb.iloc[8] = CBi.loc[CP09].values.sum()
CBi_Urb.iloc[9] = CBi.loc[CP10].values.sum()
CBi_Urb.iloc[10] = CBi.loc[CP11].values.sum()
CBi_Urb.iloc[11] = CBi.loc[CP12].values.sum()

CBi_Urb

###################################################################
#####   CBi_Urb['Cities','Towns and suburbs','Rural areas']   #####

#%%
CBi_Urb['Cities'] = CBi_Urb['CB Energy Footprint'].values * Urbanization['Cities'].values
CBi_Urb['Towns and suburbs'] = CBi_Urb['CB Energy Footprint'].values * Urbanization['Towns and suburbs'].values
CBi_Urb['Rural areas'] = CBi_Urb['CB Energy Footprint'].values * Urbanization['Rural areas'].values

CBi_Urb


