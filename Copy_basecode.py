# Authors: Andrine Roska Vallestad, Ida Bertine Rambøl, Kristian L. Karstensen
# Mail:
# Version stuff
# something 
# header stuff
#Tester her 123



#####################################################################

####      NEW ATTEMPT with COICOP categories from the start     #####

#####################################################################

#%%
# Import packages
import pandas as pd
import numpy as np
import matplotlib as plt

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

########################################
#%%
df_Y_HH_CP = (index=(regions, COICOP), columns= df_Y_HH.columns)
df_Y_HH_CP
#%%

# Making df_Y_HH_CP with COICOP categories  ### !!!


#df_F_Urb = pd.DataFrame(index=COICOP, columns=(['stressor']))

#for i in range(1, 13):
#    cp = globals()[f"CP{i:02d}"]
#    df_F_Urb.iloc[i-1] = F_by_sector.loc[cp].values.sum()



#######################################

#%%
# Import product and classification category
Category =  pd.read_excel(r"Data/Test_product_categories.xlsx", header=[0,1])#.fillna(0)
COICOP = Category.columns.get_level_values(0)

# For loop to make variables for each COICOP category in Eurostat, containing the relevant Exiobase categories
for i in range(12):
    cp_name = 'CP{:02d}'.format(i+1)
    cp_variable = Category.iloc[:, i]
    globals()[cp_name] = cp_variable.dropna('index')

CP01

#%%
##################################################################
#####                Data from Eurostat as df_Y               ####

# Import Eurostat Urbanization data
Eurostat =  pd.read_excel(r"Data/Urbanization_Eurostat.xlsx", header=[0], index_col=[0]).fillna(0)
Eurostat # Unit: Per mille = Parts per thousand = Promille

#%%
# Define final demand vectors with unit percentage
Urbanization = Eurostat/1000 # Percentage
df_Y_city = pd.DataFrame((Urbanization.loc[:,'Cities']).values, index=COICOP, columns=['Cities'])
df_Y_town = pd.DataFrame((Urbanization.loc[:,'Towns and suburbs']).values, index=COICOP, columns=['Towns and suburbs'])
df_Y_rural = pd.DataFrame((Urbanization.loc[:,'Rural areas']).values, index=COICOP, columns=['Rural areas'])



############################################################################
#####                         Defining df_F_Urb                        #####
    # Dataframe for relevant energy stressors in Norway
    # One for each urbanization category
    # (unit = TJ, see explanation and approach below)

#%%
# Making a new F Dataframe with only Norway, and excluding rows with only zeros
df_F_NOR = df_F["Norway"]
df_F_NOR = df_F_NOR.loc[(df_F_NOR!=0).any(axis=1)]

# Defining Energy relevant stressors in F_NOR 
Energy_stressors = df_F_NOR[df_F_NOR.index.get_level_values(level=0).str
                            .contains('Energy|Electricity|El|Fuel|Coal|Petroleum|hydro|wind')].index

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
  
#%%


#######################################################################################
###     Reshaping df_F frpm 92 Exiobase categories to 12 Eurostat categories        ###

# Summing up values across all regions for each sector and creating a new DataFrame with summed values for each sector
F_by_sector = pd.DataFrame((df_F_Energy_TJ.groupby(level='sector').sum()))

df_F_Urb = pd.DataFrame(index=COICOP, columns=(['stressor']))

for i in range(1, 13):
    cp = globals()[f"CP{i:02d}"]
    df_F_Urb.iloc[i-1] = F_by_sector.loc[cp].values.sum()

df_F_Urb

#%%
#######################################################################################
###     Reshaping df_Z frpm 92 Exiobase categories to 12 Eurostat categories        ###

df_Z_Nor = df_Z.loc[:, ('Norway')]

# Summing up values across all regions for each sector and creating a new DataFrame with summed values for each sector
Z_by_sector = pd.DataFrame((df_Z_Nor.groupby(level='sector').sum()))


#%%
df_Z_Urb = pd.DataFrame(index=COICOP, columns=COICOP)

for i in range(1, 13):
    for j in range(1, 13):
        cp_i = globals()[f"CP{i:02d}"]
        cp_j = globals()[f"CP{j:02d}"]
        df_Z_Urb.iloc[i-1, j-1] = Z_by_sector.loc[cp_i, cp_j].values.sum()

df_Z_Urb

#####################################################################################

#%%
df_Z_Urb

#%%
# Calculate xout
df_xout_city = (df_Z_Urb.sum(axis=1) + df_Y_city.sum(axis=1))#.fillna(0)
df_xout_city


#%%
array_xout_city = df_xout_city.values
array_xout_city



######################################################### NB: Xout =/= Xin , aka not correct!

#%%
# Calculate A-matrix
matrixZ = df_Z_Urb.values
matrixA_city = matrixZ / array_xout_city


#%% 
# Fill NaN values in matrixA with 0
matrixA_city = np.nan_to_num(matrixA_city, nan=0)
matrixA_city


#%%
# Calculate Leontief's inverse
matrixI_city = np.identity(matrixA_city.shape[0])
matrixImA_city = (matrixI_city - matrixA_city)
matrixImA_city

#%%
# Check determinant of matrixImA before inverse
print(np.linalg.det(matrixImA_city))


#%%
matrixL_city = np.linalg.inv(matrixImA_city)
matrixL_city

# Check that xout = L* (sum FD)

#%%
array_sFD = df_Y.sum(axis=1)
xout2 = matrixL@array_sFD
print(xout2)
print(array_xout)


###################################################################################################
###                         Calculating CBi for Norway and Energy Footprint                     ###


#%%
array_F_Urb = df_F_Urb.values
print(array_F_Urb.sum())


#%%
# Calculate production-based intensities, array_PBi
array_F_city = array_F_Urb.reshape(array_xout_city.shape)
array_PBi = (array_F_city / array_xout_city)      # These need to be in the same shape, hence above line
array_PBi = np.nan_to_num(array_PBi, nan=0)
print(array_PBi)

#%%
# Calculate consumption-based intensities, array_CBi
array_CBi = array_PBi @ matrixL
print(array_CBi)






########################################################################################


     #######    #           #####
    #       #   #           #    ##
    #       #   #           #      ##
    #       #   #           #      ##
    #       #   #           #    ##
     #######    ########    #####

                # STUFF

#######################################################################################
###     Reshaping df_F frpm 92 Exiobase categories to 12 Eurostat categories        ###

# Summing up values across all regions for each sector and creating a new DataFrame with summed values for each sector
F_by_sector = pd.DataFrame((df_F_Energy_TJ.groupby(level='sector').sum()))

df_F_Urb = pd.DataFrame(index=COICOP, columns=(['stressor']))

for i in range(1, 13):
    cp = globals()[f"CP{i:02d}"]
    df_F_Urb.iloc[i-1] = F_by_sector.loc[cp].values.sum()

df_F_Urb

#%%
#######################################################################################
###     Reshaping df_Z frpm 92 Exiobase categories to 12 Eurostat categories        ###

df_Z_Nor = df_Z.loc[:, ('Norway')]
df_Z_Nor

#%%

# Summing up values across all regions for each sector and creating a new DataFrame with summed values for each sector
Z_by_sector = pd.DataFrame((df_Z_Nor.groupby(level='sector').sum()))
Z_by_sector

#%%
df_Z_Urb = pd.DataFrame(index=COICOP, columns=COICOP)

for i in range(1, 13):
    for j in range(1, 13):
        cp_i = globals()[f"CP{i:02d}"]
        cp_j = globals()[f"CP{j:02d}"]
        df_Z_Urb.iloc[i-1, j-1] = Z_by_sector.loc[cp_i, cp_j].values.sum()

df_Z_Urb

#####################################################################################

#%%
df_Z_Urb

#%%
# Calculate xout
df_xout_city = (df_Z_Urb.sum(axis=1) + df_Y_city.sum(axis=1))#.fillna(0)
df_xout_city


#%%
array_xout_city = df_xout_city.values
array_xout_city



######################################################### NB: Xout =/= Xin , aka not correct!

#%%
# Calculate A-matrix
matrixZ = df_Z_Urb.values
matrixA_city = matrixZ / array_xout_city
matrixA_city

#%% 
# Fill NaN values in matrixA with 0
matrixA_city = np.nan_to_num(matrixA_city, nan=0)
matrixA_city



#%%
# Calculate Leontief's inverse
matrixI_city = np.identity(matrixA_city.shape[0])
matrixImA_city = (matrixI_city - matrixA_city)
matrixImA_city

#%%
# Check determinant of matrixImA before inverse
print(np.linalg.det(matrixImA_city))


#%%
matrixL_city = np.linalg.inv(matrixImA_city)
matrixL_city

# Check that xout = L* (sum FD)

#%%
array_sFD = df_Y.sum(axis=1)
xout2 = matrixL_city@array_sFD
print(xout2)
print(array_xout_city)


###################################################################################################
###                         Calculating CBi for Norway and Energy Footprint                     ###


#%%
array_F_Urb = df_F_Urb.values
print(array_F_Urb.sum())


#%%
# Calculate production-based intensities, array_PBi
array_F_city = array_F_Urb.reshape(array_xout_city.shape)
array_PBi = (array_F_city / array_xout_city)      # These need to be in the same shape, hence above line
array_PBi = np.nan_to_num(array_PBi, nan=0)
print(array_PBi)

#%%
# Calculate consumption-based intensities, array_CBi
array_CBi = array_PBi @ matrixL
print(array_CBi)








###################################################

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

# Check that xout = L* (sum FD)

#%%
array_sFD = df_Y.sum(axis=1)
xout2 = matrixL@array_sFD
print(xout2)
print(array_xout)


###################################################################################################
### ### ### ### ### ### ###  Calculating CBi for Norway and ENergy Footprint  ### ### ### ### ### ### ###


#%%
array_F_Energy = df_F_Energy_TJ.values
print(array_F_Energy.sum())
# LF PS7: print(arrayF_GHGs.sum()/1000000000) why 10^x ?


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
df_CBi_NOR # Norwegian Consumption Based intensities (unit?)

#%%
df_CBi_NOR.to_csv('CBi_NOR_test.csv', index=[0,1])





# Note that the units are a bit nuts - usually we want intensities as kg/â‚¬. 
# Here, we transform to meaningful units below.
 
    ### What are the current units from before?
    ### What are meaningful units for us???





# What do we do with the json files?
    # file_parameters.json
    # metadata.json


