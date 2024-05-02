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
from matplotlib import rcParams
import seaborn as sns

#%%
# Picking out the Energy Footprint for the Housing category [MWh]
EF = pd.read_csv(r"CBi_Urb.csv", header=[0], index_col=[0])
EF_CP04 = pd.DataFrame(EF.iloc[3, :].values, index=['CBi', 'EF - Cities', 'EF - Towns and suburbs', 'EF - Rural areas'], columns=['CP04'])

EF_CP04



#%%
# Import SSB dataset for average price per sqm for the different levels of ubranization
SSB= pd.read_excel(r"Data/SSB_renting_prices_2015.xlsx", header=0, index_col=[0])
SSB

#%%
# Ef [MWh] / Average price per sqm [Euro/m2]
df = pd.DataFrame(index=[''], columns=['Cities', 'Towns and suburbs', 'Rural areas'])

df.loc['', :] = ( EF_CP04.loc['CBi', 'CP04'] * SSB.iloc[0,:] ) / ( SSB.iloc[1,:] )
df

#%%
df = pd.DataFrame(index=[''], columns=['Cities', 'Towns and suburbs', 'Rural areas'])

df.loc['', :] = ( EF_CP04.loc[['EF - Cities', 'EF - Towns and suburbs', 'EF - Rural areas'], 'CP04'].values @ SSB.iloc[0,:].values ) / ( SSB.iloc[1,:] ).values
df


#%%###################################################################################

####                          Plotting with Seaborn                               ####

######################################################################################

# Setting the figure size and font adjustments
rcParams['figure.figsize'] = 8, 10 # Inches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12

# color #248b24 is the original color in the first result plot for Energy Footprint
color_palette = ['#248b24', '#1B681B', '#7FBB7F'] 


#%%################################################################
###                    Horizontal bar plot                      ###
sns.set_style("whitegrid")

plt.rcParams['figure.figsize'] = 8, 4


# Plotting the bars
plt.barh(df.columns, df.iloc[0,:], height=0.5, color=['#248b24', '#1B681B', '#7FBB7F'])

# Moving the legend to below the plot
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels, bbox_to_anchor=(0.5, -0.25), loc='upper center', borderaxespad=0, fontsize=12, ncol=len(labels))

plt.xlabel('$MWh / m^2$')

# Adjust layout to prevent clipping of labels and adjust spacing
plt.tight_layout()


plt.show()

