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
Eurostat =  pd.read_excel(r"Data/Urbanization_Eurostat.xlsx", header=[0,1], index_col=[0]).fillna(0)
Eurostat

#%%
# Urbanization categories
Urb_Cat = list(set(Eurostat.columns.get_level_values(0)))
Urb_Cat

#%%
# Import calculated CBi for Energy Footprint in Norwegian households
CBi = pd.read_excel(r"CBi_NOR_test.xlsx", header=[0], index_col=[0,1])
CBi

#%%
# Import product and classification category
Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1]).fillna(0)
Category

#%%
# Making a new DataFrame
CBi_Urb = pd.DataFrame(index=Category.columns)
CBi_Urb['CB Energy Footprint'] = 0
CBi_Urb['Cities'] = 0
CBi_Urb['Towns and suburbs'] = 0
CBi_Urb['Rural areas'] = 0
CBi_Urb

#%%
####################################
#####      CBi_Urb['CBi']      #####

#%%
CBi.loc[Category.iloc[:,0]]

#%%
Category

#%%
#list(set(Category.iloc[:,0]))

Category.iloc[:, 0]



#%%
test = CBi.loc[Category.iloc[:, 0]]
test

#%%
# Function to summarize CBi values based on Category placement
def summarize_values(CBi, Category):
    result = {}
    for col in Category.columns:
        category_name, pattern_name = col
        category_columns = Category[col].values
        pattern_values = CBi[category_columns].sum(axis=1)
        result[(category_name, pattern_name)] = pattern_values
    return pd.DataFrame(result)

# Call the function to get the summarized DataFrame
summary = summarize_values(CBi, Category)

print(summary)

