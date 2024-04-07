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
df_Y = pd.read_csv(r"Data/Y.txt", sep='\t', header=[0,1], index_col=[0,1])
df_Z = pd.read_csv(r"Data/Z.txt", sep='\t', header=[0,1], index_col=[0,1])
df_F = pd.read_csv(r"Data/F.txt", sep='\t', header=[0,1], index_col=[0,1])

    # Same note hear, header and index_col
unit_F = pd.read_csv(r"Data/unit_F.txt", sep='\t', header=0, index_col=[0,1])
unit_Z = pd.read_csv(r"Data/unit_Z.txt", sep='\t', header=0, index_col=[0,1])

#%%
display(unit_F)


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

# Calculate xout

#%%
df_xout = (df_Z.sum(axis=1) + df_Y.sum(axis=1)).fillna(0)
df_xout

#%%
df_F


#%%
array_xout = df_xout.values

array_xout

# Calculate A-matrix

#%%
matrixZ = df_Z.values
matrixA = matrixZ / array_xout


#%% 

# Fill NaN values in matrixA with 0
matrixA = np.nan_to_num(matrixA, nan=0)



# Calculate Leontief's inverse

#%%
matrixI = np.identity(matrixA.shape[0])
matrixImA = (matrixI - matrixA)

print(matrixImA)

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

#%%
print(array_xout)




# Calculate production-based intensities, array_PBi


#%%

####

# F vs F_GHG below !! NB !! TESTING and Comparing PS7

####




#%%
display(unit_F)
display(df_F)

#%%

PS7_F_GHG = pd.read_csv(r"Data/PS7/PS7_F_GHG.txt", sep='\t')

PS7_arrayF_GHG = PS7_F_GHG.values
print(PS7_arrayF_GHG.sum()/1000000000)






#####

# Løsningsforslag fortsetter under her

#####

#%%
arrayF_GHGs = arrayF_GHGs.reshape(162,)
array_PBi = arrayF_GHGs / array_xout      # These need to be in the same shape, hence above line
print(array_PBi)

# Calculate consumption-based intensities, array_CBi

#%%
array_CBi = array_PBi@matrixL
print(array_CBi)

# Note that the units are a bit nuts - usually we want intensities as kg/â‚¬. 
# Here, we transform to meaningful units below. 

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
