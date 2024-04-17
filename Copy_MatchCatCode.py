# Authors: Andrine Roska Vallestad, Ida Bertine Rambøl, Kristian L. Karstensen
# Mail:
# Version stuff
# something 
# header stuff
# Tester her 123


#%%
# Import packages
import pandas as pd
import numpy as np
import matplotlib as plt


#%%
# Import calculated CBi for Energy Footprint in Norwegian households
#CBi = pd.read_excel(r"CBi_NOR_test.xlsx", header=[0], index_col=[0])
CBi = pd.read_csv(r"Data/CBi_NOR.csv", header=[0], index_col=[0])

# Import overview of COICOP and production categories
Category =  pd.read_excel(r"Data/Product_categories.xlsx", header=[0,1])#.fillna(0)
COICOP = Category.columns.get_level_values(0)

#%%
# Import Eurostat data with distribution of consumption expenditure for different urbanizations
Eurostat =  pd.read_excel(r"Data/Urbanization_Eurostat.xlsx", header=[0], index_col=[0]).fillna(0)
Eurostat # Unit Per mille = Parts per thousand = Promille
Urb_sum = Eurostat.sum(axis=0)
Urb_sum

#%%
# Data for expenditure from Juudit's Eurostat, Sweden 2015 as example
    # Cities: 16430.86
    # Towns and suburbs: 16339.03
    # Rural areas: 15718.58

# Making a new DataFrame with expenditure using the data commented above
Expenditure = pd.DataFrame(index=COICOP, columns=Eurostat.columns)
Expenditure['Cities'] = 16430.86 * Eurostat.loc[:,'Cities'].values/1000
Expenditure['Towns and suburbs'] = 16339.03 * Eurostat.loc[:,'Towns and suburbs'].values/1000
Expenditure['Rural areas'] = 15718.58 * Eurostat.loc[:,'Rural areas'].values/1000
Expenditure


#%%
###################################################################
####                      CBi_Urb['CBi']                       ####

# Picking out the first COICOP category to test before for loop below
    # CP01 = Category.iloc[:, 0]
    # CP01 = CP01.dropna('index')

# For loop to make variables for each COICOP category in Eurostat
for i in range(12):
    cp_name = 'CP{:02d}'.format(i+1)
    cp_variable = Category.iloc[:, i]
    globals()[cp_name] = cp_variable.dropna('index')


#%%
# Summing up the relevant values for each COICOP category   UNIT = TJ / Valuta

CBi_Urb = pd.DataFrame(index=COICOP, columns=['CBi'])              # Only COICOP category CPxx
#CBi_Urb = pd.DataFrame(index=Category.columns, columns=['CBi'])     # CPxx plus name of COICOP category

for i in range(1, 13):
    cp = globals()[f"CP{i:02d}"]
    CBi_Urb.iloc[i-1] = CBi.loc[cp].values.sum()

CBi_Urb

#%%
########################################################################
####       CBi_Urb['Cities','Towns and suburbs','Rural areas']      ####

#%%

CBi_Urb['Cities'] = CBi_Urb['CBi'].values * Expenditure['Cities'].values
CBi_Urb['Towns and suburbs'] = CBi_Urb['CBi'].values * Expenditure['Towns and suburbs'].values
CBi_Urb['Rural areas'] = CBi_Urb['CBi'].values * Expenditure['Rural areas'].values

CBi_Urb
