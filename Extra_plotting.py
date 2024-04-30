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

# Energy Footprint / (Average price per m2) [MWh/(Euro/m2)]

        # print(sns.color_palette("pastel6").as_hex())     # see colors as hex for indvidual plots

# Setting the figure size and font adjustments
rcParams['figure.figsize'] = 8, 10 # Inches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12

# color nr. 2 is the original color in the first result plot 
# #248b24
#color_palette = ['#23b23c', '#33FF57', '#84ff9a']
color_palette = ['#248b24', '#1B681B', '#7FBB7F'] 


#%%################################################################
###                    Horizontal bar plot                      ###
sns.set_style("whitegrid")

plt.rcParams['figure.figsize'] = 8, 4

# Determine the number of bars
n_bars = df.shape[0]

# Width of each bar
bar_width = 0.5

# Plotting the bars
ax = df.plot(kind='barh', color=color_palette, width=bar_width)


# Moving the legend to below the plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(0.5, -0.25), loc='upper center', borderaxespad=0, fontsize=12, ncol=len(labels))

# Adjusting y-ticks
#plt.yticks(np.arange(0, 6, 1.0))
# Rotating X-axis labels
plt.xticks(rotation=360)


plt.xlabel('$MWh / m^2$')

# Adjust layout to prevent clipping of labels and adjust spacing
plt.tight_layout()

plt.show()


#%%##################################################################

plt.rcParams['figure.figsize'] = 8, 4

# Width of each bar
bar_width = 0.5

# Plotting the bars
ax = df.plot(kind='bar', color=color_palette, width=bar_width)


# Moving the legend to below the plot
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels, bbox_to_anchor=(0.5, -0.25), loc='upper center', borderaxespad=0, fontsize=12, ncol=len(labels))

# Adjusting y-ticks
#plt.yticks(np.arange(0, 6, 1.0))

plt.ylabel('$MWh / m^2$')

# Adjust layout to prevent clipping of labels and adjust spacing
plt.tight_layout()

plt.show()
