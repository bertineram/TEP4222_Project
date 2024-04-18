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
df1 = pd.read_csv(r"1_CBi_Urb.csv", header=[0], index_col=[0])
df2 = pd.read_csv(r"2_CBi_Urb.csv", header=[0], index_col=[0])
df3 = pd.read_csv(r"3_CBi_Urb.csv", header=[0], index_col=[0])

display(df1)
display(df2)
display(df3)

#%%
Category =  pd.read_excel(r"Data/1_product_categories.xlsx", header=[0,1])#.fillna(0)
COICOP = Category.columns.get_level_values(0)
COICOP

#%%
df1

#%%
# "Pivoting" the table: (12,4) -> (3,12)
df = pd.DataFrame(index=['Cities', 'Towns and suburbs', 'Rural areas'], columns=COICOP)

df.loc['Cities'] = df3.loc[:,'Cities'].values
df.loc['Towns and suburbs'] = df3.loc[:,'Towns and suburbs'].values
df.loc['Rural areas'] = df3.loc[:,'Rural areas'].values

df

#%%
###############################################
######      Plotting with Seaborn        ######



# Apply the default theme       # ?
#sns.set_theme() # y / n ?       # ?


#%%

# Set the size of the figure
#plt.figure(figsize=(120, 4))  
rcParams['figure.figsize'] = 11, 4 # Inches
#rcParams['figure.figsize'] = 40, 4

rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 20        # does not work on axes and 


# Create the horizontal bar plot
ax = df.plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))

# Get legend handles and labels
handles, labels = ax.get_legend_handles_labels()

# Reverse handles and labels for legend
ax.legend(handles[::-1], labels[::-1], title='COICOP', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=12)

# Set font size for axes labels
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)

#plt.ylabel('UNIT')
#plt.xlabel('Urbaization')
#plt.title('Consumption Based Energy Footprint', fontsize=14) #fontstyle ='TNR'

# Save the plot as a PDF file
#plt.savefig('TEST_bar_plot.pdf', dpi=300, bbox_inches='tight')



        #   NB: Font style and size ! 
plt.show()


#%%
# colorblind, Spectral

rcParams['figure.figsize'] = 10, 10

ax = df3.plot(kind = 'bar', stacked = True, color= sns.color_palette('colorblind', n_colors=3))
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='COICOP', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

#plt.ylabel('UNIT')
#plt.xlabel('Urbaization')
plt.title('Consumption Based Energy Footprint', fontsize=14) #fontstyle ='TNR'

