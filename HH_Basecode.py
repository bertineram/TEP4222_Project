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
import matplotlib.pyplot as plt

#%%
# Import data
df_Y = pd.read_csv(r"Data/Y.txt", sep='\t', header=[0,1], index_col=[0,1])
df_Z = pd.read_csv(r"Data/Z.txt", sep='\t', header=[0,1], index_col=[0,1])
df_F = pd.read_csv(r"Data/F.txt", sep='\t', header=[0,1], index_col=[0])

unit_F = pd.read_csv(r"Data/unit_F.txt", sep='\t', header=0, index_col=0)
unit_Z = pd.read_csv(r"Data/unit_Z.txt", sep='\t', header=0, index_col=[0,1])

#%%
regions = list(set(df_Z.index.get_level_values(0)))
products = list(set(df_Z.index.get_level_values(1)))
FD_categories = list(set(df_Y.columns.get_level_values(1)))

#%%
df_Y_HH = df_Y.loc[:, (regions, 'Households consumption')]
df_Y_HH


###########################################################################
###                   Defining df_F(_NOR)_ENERGY_TJ                      ####
    # *Datframe for relevant energy stressors in Norway 
    #  (unit = TJ, see explanation and approach below)

#%%
# Making a new F Dataframe with only Norway, and excluding rows with only zeros
df_F_NOR = df_F["Norway"]
df_F_NOR = df_F_NOR.loc[(df_F_NOR!=0).any(axis=1)]

# Defining Energy relevant stressors in df_F_NOR
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
df_F_Energy_TJ = df_F.loc[unit_dataframes[unique_units[0]].index].sum(axis=0)
df_F_Energy_TJ

###########################################################
###                 Calculating x, A and L              ###

#%%
# Calculate xout
df_xout = (df_Z.sum(axis=1) + df_Y_HH.sum(axis=1)).fillna(0)

df_xout_NOR = df_xout['Norway']
df_xout_NOR

#%%
array_xout = df_xout.values
array_xout

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

# Check that xout = xout2

#%%
array_sFD = df_Y_HH.sum(axis=1)
xout2 = matrixL@array_sFD
print(xout2)
print(array_xout)


###################################################################################################
###                      Calculating CBi for Norway and Energy Footprint                        ###


#%%
array_F_Energy = df_F_Energy_TJ.values
print(array_F_Energy.sum())

#%%
# Calculate production-based intensities, array_PBi
array_F_Energy = array_F_Energy.reshape(array_xout.shape)
array_PBi = (array_F_Energy / array_xout)      # These need to be in the same shape, hence above line
array_PBi = np.nan_to_num(array_PBi, nan=0)
print(array_PBi)

#%%
# Calculate consumption-based intensities, array_CBi
array_CBi = array_PBi @ matrixL
print(array_CBi)

#%%
df_CBi = pd.DataFrame(array_CBi, index=df_F.columns, columns=(["CBi"]))
df_CBi

#%%
df_CBi_NOR = df_CBi.loc['Norway']
df_CBi_NOR # Norwegian Consumption Based intensities (unit = TJ / Valuta ?)

#%%
df_CBi_NOR.to_csv('New_CBi_NOR.csv', index=[0,1])
