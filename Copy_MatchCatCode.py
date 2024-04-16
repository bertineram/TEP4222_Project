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
# Import calculated CBi for Energy Footprint in Norwegian households
#CBi = pd.read_excel(r"CBi_NOR_test.xlsx", header=[0], index_col=[0])
CBi = pd.read_csv(r"New_CBi_NOR.csv", header=[0], index_col=[0])

df_Y = pd.read_csv(r"Data/Y.txt", sep='\t', header=[0,1], index_col=[0,1])

Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1])#.fillna(0)
COICOP = Category.columns.get_level_values(0)

# For loop to make variables for each COICOP category in Eurostat, containing the relevant Exiobase categories
for i in range(12):
    cp_name = 'CP{:02d}'.format(i+1)
    cp_variable = Category.iloc[:, i]
    globals()[cp_name] = cp_variable.dropna('index')


##################################################
#%%
df_Y_Nor_HH = df_Y.loc[:, ('Norway', 'Households consumption')]
df_Y_Nor2_HH = pd.DataFrame((df_Y_Nor_HH.groupby(level='sector').sum()))


#%%
df_Y_NOR_HH = pd.DataFrame(index=COICOP, columns=(['Final demand, HH Norway']))

for i in range(1, 13):
    cp = globals()[f"CP{i:02d}"]
    df_Y_NOR_HH.iloc[i-1] = df_Y_Nor2_HH.loc[cp].values.sum()

df_Y_NOR_HH


#%%
df_Y_NOR_HH['Percentage %'] = (df_Y_NOR_HH.loc[:, 'Final demand, HH Norway'])/(df_Y_NOR_HH.loc[:, 'Final demand, HH Norway'].sum())
df_Y_NOR_HH


######################################


#%%
# Import Eurostat Urbanization data
Eurostat =  pd.read_excel(r"Data/Urbanization_Eurostat.xlsx", header=[0], index_col=[0]).fillna(0)
Eurostat # Unit Per mille = Parts per thousand = Promille
Urb_sum = Eurostat.sum(axis=0)
Urb_sum

#%%
Urbanization = Eurostat/1000 # Percentage
Urbanization


#%%
# Urbanization categories
Urb_Cat = list(set(Eurostat.columns.get_level_values(0)))
Urb_Cat


#%%
# Import product and classification category
Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1])#.fillna(0)
Category

#%%
COICOP = Category.columns.get_level_values(0)
COICOP

#%%
# Making a new DataFrame
CBi_Urb = pd.DataFrame(index=Category.columns)
CBi_Urb['CB Energy Footprint'] = 0
CBi_Urb


#%%
##################################################
#####              CBi_Urb['CBi']            #####

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

#CBi_Urb = pd.DataFrame(index=COICOP, columns=['CBi'])              # Only COICOP category CPxx
CBi_Urb = pd.DataFrame(index=Category.columns, columns=['CBi'])     # CPxx plus name of COICOP category

for i in range(1, 13):
    cp = globals()[f"CP{i:02d}"]
    CBi_Urb.iloc[i-1] = CBi.loc[cp].values.sum()


#%%

CBi_Urb['CBi New'] = 0
for i in range(1, 13):
    cp = globals()[f"CP{i:02d}"]
    CBi_Urb.iloc[i-1, 1] = CBi_new.loc[cp].values.sum()

CBi_Urb

######

#%%
CBi_Urb.sum(axis=0)


#%%

CBi_Urb['CBi %'] = CBi_Urb['CBi']/(CBi_Urb['CBi'].sum())

CBi_Urb

#######


#%%
###################################################################
#####   CBi_Urb['Cities','Towns and suburbs','Rural areas']   #####

Urbanization


#%%

CBi_sum = CBi_Urb.loc[:, 'CBi'].sum()
CBi_row1 = Urbanization.iloc[0,:].values
CBi_row2 = Urbanization.iloc[1,:].values

#%%

y = np.array([CBi_sum, CBi_Urb.iloc[0, 0], CBi_Urb.iloc[1, 0]])
A = np.array([[1,1,1], CBi_row1, CBi_row2])

x = np.linalg.inv(A) @ y
x


#%%

# NB: Dilemma, not accurate approach !

CBi_Urb['Cities'] = CBi_Urb['CBi'].values * Urbanization['Cities'].values
CBi_Urb['Towns and suburbs'] = CBi_Urb['CBi'].values * Urbanization['Towns and suburbs'].values
CBi_Urb['Rural areas'] = CBi_Urb['CBi'].values * Urbanization['Rural areas'].values

CBi_Urb

#%%
Urbanization