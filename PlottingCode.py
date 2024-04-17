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
df1 = pd.read_csv(r"1_CBi_Urb.csv", header=[0], index_col=[0])
df2 = pd.read_csv(r"2_CBi_Urb.csv", header=[0], index_col=[0])
df3 = pd.read_csv(r"3_CBi_Urb.csv", header=[0], index_col=[0])

#%%
display(df1)
display(df2)
display(df3)

#%%
# Making a new DataFrame
    # Import finished dataset here instead 
    # Ex: CBi = pd.read_excel(r"CBi_NOR_test.xlsx", header=[0], index_col=[0])

Category =  pd.read_excel(r"Data/1_product_categories.xlsx", header=[0,1])#.fillna(0)
COICOP = Category.columns.get_level_values(0)
COICOP

#%%

#CBi_Urb = pd.DataFrame(index=Category.columns, columns=['CB En FP','City','Town','Rural'])
CBi_Urb = pd.DataFrame(columns=COICOP, index=['City','Town','Rural'])
CBi_Urb


# .pivot flip dataframe
#%%
Random = np.random.randint(low=0, high=100, size=(CBi_Urb.shape))
df = pd.DataFrame(Random, index=CBi_Urb.index, columns=CBi_Urb.columns)

#%%
df1

#%%
df


#%%
Hei = pd.DataFrame(index=['Cities', 'Towns and suburbs', 'Rural areas'], columns=COICOP)
Hei



#%%
###############################################
######      Plotting with Seaborn        ######

#%%
import seaborn as sns



ax = df1.plot(kind = 'bar', stacked = True, color= sns.color_palette('Spectral', n_colors=12))
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='COICOP', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

#plt.ylabel('UNIT')
#plt.xlabel('Urbaization')
plt.title('Consumption Based Energy Footprint', fontsize=14) #fontstyle ='TNR'












# Apply the default theme
#sns.set_theme()

#%%
# colorblind, Spectral


ax = df1.plot(kind = 'bar', stacked = True, color= sns.color_palette('Spectral', n_colors=12))
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='COICOP', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

#plt.ylabel('UNIT')
#plt.xlabel('Urbaization')
plt.title('Consumption Based Energy Footprint', fontsize=14) #fontstyle ='TNR'



#%%
CBi_new = pd.read_csv(r"1_CBi_Urb.csv", header=[0], index_col=[0])

CBi_new

#%%
ax = df1.plot(kind = 'bar', color= sns.color_palette('Spectral', n_colors=12))
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='COICOP', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

#plt.ylabel('UNIT')
#plt.xlabel('Urbaization')
plt.title('Consumption Based Energy Footprint', fontsize=14) #fontstyle ='TNR'


