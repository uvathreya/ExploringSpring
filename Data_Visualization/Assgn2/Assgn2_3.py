import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('./estimated_hiv_prevelance_indicator_modified.csv')
data_df = pd.DataFrame(data)
df = data_df
#print(data_df.head())

df_sub2 = pd.DataFrame(columns=['continent','avgCval'])
u_continent = df.continent.unique()
for i in u_continent:
    df_sub = df[df.continent == i]
    total_countries = len(df_sub.country.unique())
    #print(i)
    #print(total_countries)
    df_sub.drop(columns=['continent', 'country'])
    df_sub2 = df_sub2.append({'continent' : i,'avgCval' : df_sub.sum(axis=1).sum()/total_countries},ignore_index=True)
    
#print(df_sub2)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot( 'continent', 'avgCval', data=df_sub2, marker='o', markerfacecolor='blue', color='skyblue', linewidth=4)
for i,j in df_sub2.avgCval.items():
    ax.annotate(str(round(j,2)), xy=(i, j))
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

df_sub1 = pd.DataFrame()
df_final2 = pd.DataFrame()
u_continent = df.continent.unique()
for i in u_continent:
    df_sub = df[df.continent == i]
    clenl = list(df_sub.country)
    clen=len(df_sub.country)-1
    df_sub1 = df_sub.transpose()
    df_subh = df_sub1.iloc[:2,:]
    df_subh['avgvl'] = ''
    df_sub1 = df_sub1.iloc[2:,:]
    df_sub1['avgvl'] = 0
    df_sub1['avgvl'] = df_sub1.mean(axis=1)
    df_final = df_subh.append(df_sub1).transpose().tail(1)
    df_final['continent'] = i
    df_final2 = df_final2.append(df_final)
df_final2 = df_final2.drop(columns=['country'])
df_final3 = df_final2.transpose()
df_final3.index.name = 'newhead'
df_final3.reset_index(inplace=True)
new_header = df_final3.iloc[0] #grab the first row for the header
df_final3 = df_final3[1:] #take the data less the header row
df_final3.columns = new_header #set the header row as the df header

print(df_final3)

# style
plt.style.use('seaborn-darkgrid')
 
# create a color palette
palette = plt.get_cmap('Set1')
 
# multiple line plot
num=0
for column in df_final3.drop('continent', axis=1):
    num+=1
    plt.plot(df_final3['continent'], df_final3[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
 
# Add legend
plt.legend(loc=2, ncol=2)
 
# Add titles
plt.title("Yearly Distribution of HIV Prevelance ", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("YEARS ")
plt.ylabel("Average Values")
plt.xticks(list(df_final3.continent),rotation=90)
ax.xaxis.set_ticks_position('none')
df_final2.to_csv('./estimated_hiv_prevelance_indicator_modified_1.csv')

df_final2

df_final4 = pd.DataFrame()
df_final4['continent'] = df_final2.continent
for i in range(1,(len(df_final2.columns)-2)):
    strg = df_final2.columns[i] + '-' + df_final2.columns[i+1]
    df_final4[strg] = df_final2[df_final2.columns[i]]-df_final2[df_final2.columns[i+1]]
#print(df_final4)

df_final4 = df_final4.transpose()
new_header = df_final4.iloc[0] #grab the first row for the header
df_final4 = df_final4[1:] #take the data less the header row
df_final4.columns = new_header #set the header row as the df header
df_final3.index.name = 'newhead'
df_final3.reset_index(inplace=True)

df_final4.index.name = 'newhead'
df_final4.reset_index(inplace=True)
#print(df_final4)

# style
plt.style.use('seaborn-darkgrid')
 
# create a color palette
palette = plt.get_cmap('Set1')
 
# multiple line plot
num=0
for column in df_final4.drop('newhead', axis=1):
    num+=1
    plt.plot(df_final4['newhead'], df_final4[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
 

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Add legend
ax = plt.subplot(111)
ax.legend(loc='lower left', bbox_to_anchor=(1, 0.5))
#plt.legend(loc=1, ncol=8)


#box = ax.get_position()
#ax.set_position([box.x0, box.y0 + box.height * 0.1,
#                 box.width, box.height * 0.9])

# Add titles
plt.title("Country Distribution of HIV Prevelance ", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("YEARS ")
plt.ylabel("Average difference Values")
plt.xticks(list(df_final4.newhead),rotation=90)
ax.xaxis.set_ticks_position('none') 
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

