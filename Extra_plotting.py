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
EF_CP04 = pd.DataFrame(EF.iloc[3, [1,2,3]].values, index=['Cities', 'Towns and suburbs', 'Rural areas'], columns=['CP04'])
display(EF_CP04)



EF_CP04.iloc[0,:].values

#%%
# Import SSB dataset for average price per sqm for the different levels of ubranization
SSB_sqm_price= pd.read_excel(r"Data/SSB_Sqm_12_22.xlsx", header=0, index_col=[0])
SSB_sqm_price

#%%
# Ef [MWh] / Average price per sqm [Euro/m2]
df = pd.DataFrame(index=SSB_sqm_price.index, columns=EF_CP04.index)
df.loc[2012, :] = EF_CP04.iloc[0,:].values / SSB_sqm_price.loc[2012, :]
df.loc[2022, :] = EF_CP04.iloc[0,:].values / SSB_sqm_price.loc[2022, :]
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
color_palette = ['#23b23c', '#33FF57', '#84ff9a'] 

#%%################################################################
###                     Vertical bar plot                       ###

rcParams['figure.figsize'] = 8, 4

ax = df.plot(kind = 'bar', color=color_palette)#, color= sns.color_palette('colorblind', n_colors=3))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='Level of urbanization', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

plt.yticks(np.arange(0, 6, 1.0))

# Rotating X-axis labels
plt.xticks(rotation = 360)

plt.ylabel('MWh / (Euro / $m^2$)')

plt.show()

#plt.xlabel('---')
#plt.title('', fontsize=12)

#%%################################################################
###                     Vertical bar plot                       ###
sns.set_style("whitegrid")

plt.rcParams['figure.figsize'] = 8, 4

# Determine the number of bars
n_bars = df.shape[0]

# Width of each bar
bar_width = 0.5

# Plotting the bars
ax = df.plot(kind='bar', color=color_palette, width=bar_width)

# Remove vertical grid lines
ax.grid(axis='x', linestyle='-')

# Moving the legend to below the plot
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(0.5, -0.15), loc='upper center', borderaxespad=0, fontsize=12, ncol=len(labels))

# Adjusting y-ticks
plt.yticks(np.arange(0, 6, 1.0))

# Rotating X-axis labels
plt.xticks(rotation=360)

plt.ylabel('MWh / (Euro / $m^2$)')

plt.tight_layout()  # Adjust layout to prevent clipping of labels

plt.show()

