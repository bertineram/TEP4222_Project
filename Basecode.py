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
# Import data

    # Note:  a bit unsure aboute header and index_col, need to double check
df_Y = pd.read_csv(r"Data/Y.txt", sep='\t', header=[0,1], index_col=[0,1])
df_Z = pd.read_csv(r"Data/Z.txt", sep='\t', header=[0,1], index_col=[0,1])
df_F = pd.read_csv(r"Data/F.txt", sep='\t', header=[0,1], index_col=[0]) # Changed here from index_col=[0,1] to index_col=[0]

    # Same note hear, header and index_col
unit_F = pd.read_csv(r"Data/unit_F.txt", sep='\t', header=0, index_col=0)
unit_Z = pd.read_csv(r"Data/unit_Z.txt", sep='\t', header=0, index_col=[0,1])





    ###################################################
############    DEFINING df_F_NOR_ENERGY_TJ   ############
    # *Datframe for relevant energy stressors in Norway 
    #  (unit = TJ, see explanation and approach below)

#%%
display(unit_F)

#%%
# Making a new F Dataframe with only Norway, and excluding rows with only zeros
df_F_NOR = df_F["Norway"]
df_F_NOR = df_F_NOR.loc[(df_F_NOR!=0).any(axis=1)]

#%%
# Defining Energy relevant stressors in F 
Energy_stressors = df_F_NOR[df_F_NOR.index.get_level_values(level=0).str
                            .contains('Energy|Electricity|El|Fuel|Coal|Petroleum|hydro|wind')].index 

display(Energy_stressors)

#%%
# Checking unit of Energy_stressors
Energy_stressor_unit = unit_F.loc[(Energy_stressors.values)]

unique_units = Energy_stressor_unit.iloc[:, 0].unique()

display(unique_units)

# We have three different types of units: ['TJ' 'kt' 'Mm3']


#%%
# Initialize an empty dictionary to store DataFrames for each unit
unit_dataframes = {}

# Iterate over unique units
for unit in unique_units:
    # Filter the DataFrame based on the current unit
    unit_df = Energy_stressor_unit[Energy_stressor_unit.iloc[:, 0] == unit]
    
    # Store the filtered DataFrame in the dictionary with the unit as key
    unit_dataframes[unit] = unit_df.copy()

display(unit_dataframes)


#%%
display(unit_dataframes[unique_units[0]]) # 283 different stressors in TJ
display(unit_dataframes[unique_units[1]]) # Extraction of resources in kt
display(unit_dataframes[unique_units[2]]) # Water use in maufacturing for electrical machinery in Mm3


#%%
# We continue with TJ as unit as this seems most accurate

df_F_NOR_Energy_TJ = df_F_NOR.loc[unit_dataframes[unique_units[0]].index].sum(axis=0)

df_F_NOR_Energy_TJ

# NB!!! These values does not seem accurate
# Several zero's (Ex: Private households with employed persons (95), Extra-territorial organizations and bodies)
# High variation, everything from 0.13 to 12842.30

# Why? 


############    DEFINING df_F_NOR_ENERGY_TJ   ############
    ###################################################


#%%
regions = list(set(df_Z.index.get_level_values(0)))
products = list(set(df_Z.index.get_level_values(1)))
FD_categories = list(set(df_Y.columns.get_level_values(1)))


#%%

# Collecting product list as csv 

#df_Products = pd.DataFrame()
#df_Products['Products'] = products

#display(df_Products)

#df_Products.to_csv('Products_new.csv', index=0)


#%%
# Calculate xout
df_xout = (df_Z.sum(axis=1) + df_Y.sum(axis=1)).fillna(0)

df_xout_NOR = df_xout['Norway']
df_xout_NOR


#%%
array_xout = df_xout.values
array_xout

array_xout_NOR = df_xout_NOR.values

#%%
# Calculate A-matrix
matrixZ = df_Z.values
matrixA = matrixZ / array_xout


#%% 

# Fill NaN values in matrixA with 0
matrixA = np.nan_to_num(matrixA, nan=0)
matrixA


#%%
# Calculate Leontief's inverse
matrixI = np.identity(matrixA.shape[0])
matrixImA = (matrixI - matrixA)

matrixImA

#%%

# Check determinant of matrixImA before inverse
print(np.linalg.det(matrixImA))


#%%
matrixL = np.linalg.inv(matrixImA)

matrixL

# Check that xout = L* (sum FD)

#%%
array_sFD = df_Y.sum(axis=1)
xout2 = matrixL@array_sFD
print(xout2)
print(array_xout)



###################################################################################################
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

### ### ### ### ### ### ###  Attempt to adapt to Energy and Norway  ### ### ### ### ### ### ###

    ###     ###     ###     Code still under progress, debugging needed     ###     ###     ###

#%%
array_F_Energy = df_F_NOR_Energy_TJ.values
print(array_F_Energy.sum())
# LF PS7: print(arrayF_GHGs.sum()/1000000000) why 10^x ?



#%%
# Calculate production-based intensities, array_PBi

array_F_Energy = array_F_Energy.reshape(array_xout_NOR.shape)

array_PBi = (array_F_Energy / array_xout_NOR)      # These need to be in the same shape, hence above line

array_PBi = np.nan_to_num(array_PBi, nan=0)

print(array_PBi)



#%% 
df_matrixL = pd.DataFrame(matrixL, index=df_F.columns, columns=df_F.columns)
np_matrixL_NOR = df_matrixL["Norway"].to_numpy()

np_matrixL_NOR

#%%
print(array_PBi.shape)
print(np_matrixL_NOR.shape)

#%%
# Calculate consumption-based intensities, array_CBi
array_CBi = array_PBi @ np_matrixL_NOR
print(array_CBi)

# Note that the units are a bit nuts - usually we want intensities as kg/â‚¬. 
# Here, we transform to meaningful units below. 

    ### WHat are meaningful units for us???

# Calculate PBA and CBA emissions (Mt)

#%%
PBA_GHGs = arrayF_GHGs/1000000000
CBA_GHGs = array_sFD*array_CBi/1000000000

# Check that CBA and PBA give the same total amount of emissions at global level

#%%
CBA = CBA_GHGs.sum(axis=0)
print(CBA)



#%%

# What do we do with the json files?
    # file_parameters.json
    # metadata.json


# Old code below
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
###################################################################################################


#%%
arrayF_GHGs = df_F_NOR_Energy_TJ.values
print(arrayF_GHGs.sum())
# LF: print(arrayF_GHGs.sum()/1000000000) why 10^x ?



#%%
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# This does not work

arrayF_GHGs = arrayF_GHGs.reshape(array_xout.shape)
array_PBi = arrayF_GHGs / array_xout      # These need to be in the same shape, hence above line
print(array_PBi)
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

#%%

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

# New attempt, only Norway

arrayF_GHGs = arrayF_GHGs.reshape(array_xout_NOR.shape)

array_PBi = (arrayF_GHGs / array_xout_NOR)      # These need to be in the same shape, hence above line
print(array_PBi)

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

#%% 
matrixL.shape

#%%
# Calculate consumption-based intensities, array_CBi
array_CBi = array_PBi@matrixL
print(array_CBi)

# Note that the units are a bit nuts - usually we want intensities as kg/â‚¬. 
# Here, we transform to meaningful units below. 

    ### WHat are meaningful units for us???

# Calculate PBA and CBA emissions (Mt)

#%%
PBA_GHGs = arrayF_GHGs/1000000000
CBA_GHGs = array_sFD*array_CBi/1000000000

# Check that CBA and PBA give the same total amount of emissions at global level

#%%
CBA = CBA_GHGs.sum(axis=0)
print(CBA)



#%%

# What do we do with the json files?
    # file_parameters.json
    # metadata.json
