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
CBi_NOR = pd.read_csv(r"Data/CBi_NOR.csv", header=[0], index_col=[0])
CBi_NOR

#%%
Category =  pd.read_excel(r"Data/3_product_categories.xlsx", header=[0,1])#.fillna(0)
COICOP = Category.columns.get_level_values(0)

#%%
# "Pivoting" the table: (12,4) -> (3,12)
df = pd.DataFrame(index=['Cities', 'Towns and suburbs', 'Rural areas'], columns=COICOP)

df.loc['Cities'] = df3.loc[:,'Cities'].values
df.loc['Towns and suburbs'] = df3.loc[:,'Towns and suburbs'].values
df.loc['Rural areas'] = df3.loc[:,'Rural areas'].values

df


#%%###################################################################################

####                          Plotting with Seaborn                               ####

######################################################################################


        # print(sns.color_palette("pastel6").as_hex())     # see colors as hex for indvidual plots


# Apply the default theme       # ?
#sns.set_theme() # y / n ?       # ?

# Setting the figure size and font adjustments
rcParams['figure.figsize'] = 8, 10 # Inches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12



#%%##################################################################
###                     Horizontal bar plot                       ###

# Setting the figure size and font adjustments
rcParams['figure.figsize'] = 10, 4.2 # Inches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12        # does not work on axes and legend ?


# Create the horizontal bar plot (barh (horizontal) vs bar (vertical))
ax = df.plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))

# PLot legend outside of the plot
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=12)

# Set font size for axes labels
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)

#plt.ylabel('UNIT')
#plt.xlabel('---')
#plt.title('Consumption Based Energy Footprint', fontsize=14) #? # Title on plot or in text document?  # ?

# Save the plot as a PDF file
#plt.savefig('TEST_bar_plot.pdf', dpi=300, bbox_inches='tight')

plt.show()



#%%################################################################
###                     Vertical bar plot                       ###

rcParams['figure.figsize'] = 10, 10

ax = df3.plot(kind = 'bar', stacked = True)#, color= sns.color_palette('colorblind', n_colors=3))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='Level of urbanization', bbox_to_anchor=(1, 1), loc=2, borderaxespad=0, fontsize=14)

#plt.ylabel('UNIT')
#plt.xlabel('---')
plt.title('Consumption Based Energy Footprint', fontsize=12) #fontstyle ='TNR'



#%%############################################################################################
###                             Plotting the 92 Exiobase categories                         ###

CBi = CBi_NOR.drop(index=['Inland water transportation services', 'Nuclear fuel'])
CBi

#%%
# Set the size of the figure
rcParams['figure.figsize'] = 8, 10 # Inches
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 12        # does not work on axes and legend ?

# Create the horizontal bar plot (barh (horizontal) vs bar (vertical))
ax = CBi.sort_values(by=['CBi'], ascending=True).plot(kind='barh', color='red')#, color=sns.color_palette('Spectral', n_colors=12))

# Set font size for axes labels
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)

plt.xlabel('Consumption Based index (TJ/M.Eur)')
#plt.ylabel('---')
#plt.title('Consumption Based Energy Footprint', fontsize=14) #? # Title on plot or in text document?  # ?

# Save the plot as a PDF file
#plt.savefig('TEST_bar_plot.pdf', dpi=300, bbox_inches='tight')

plt.show()



#%%###########################################################################################
###                           Plotting each category [TJ / M. Eur]                         ###

# For loop to make variables for each COICOP category in Eurostat
for i in range(12):
    cp_name = 'CP{:02d}'.format(i+1)
    cp_variable = Category.iloc[:, i]
    globals()[cp_name] = cp_variable.dropna('index')

#%%
ax = CBi.loc[CP01].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP02].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()


#%%
ax = CBi.loc[CP03].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP04].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP05].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP06].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP07].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()


#%%
ax = CBi.loc[CP08].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP09].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP10].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP11].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()

#%%
ax = CBi.loc[CP12].sort_values(by=['CBi'], ascending=True).plot(kind='barh', stacked=True, color=sns.color_palette('Spectral', n_colors=12))
plt.show()