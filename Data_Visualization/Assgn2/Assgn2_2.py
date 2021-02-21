import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

hiv_prev_data = pd.read_csv('./estimated_hiv_prevelance_indicator_modified.csv')
sel_cols = ['country', 'continent', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011']
hiv_prev_data_2000_2011 = hiv_prev_data.loc[:, sel_cols]
hiv_prev_data_2000_2011['mean_ind_val']= hiv_prev_data_2000_2011.iloc[:,2:13].mean(axis=1)

df = hiv_prev_data_2000_2011
df_sub2 = pd.DataFrame()
u_continent = df.continent.unique()
for i in u_continent:
    df_sub = df[df.continent == i]
    df_sub1 = df_sub[df_sub['mean_ind_val'] == df_sub['mean_ind_val'].max()]
    df_sub2 = df_sub2.append(df_sub1)
    

df_sub3 = df_sub2[['continent', 'mean_ind_val', 'country']] 
#print(df_sub3)

objects1 = list(df_sub3.continent)
y_values1 = np.arange(len(list(df_sub3.continent)))
x_values1 = list(df_sub3.mean_ind_val)
str11 = list(df_sub3.country)
str21 = list(round(df_sub3.mean_ind_val,2))

res1 = [i + ' - ' +  str(j) for i, j in zip(str11, str21)] 

for i in range(len(res1)): # your number of bars
    plt.text(x = x_values1[i], #takes your x values as horizontal positioning argument 
    y = y_values1[i], #takes your y values as vertical positioning argument 
    s = res1[i], # the labels you want to add to the data
    size = 9) # font size of datalabels


plt.barh(y_values1, x_values1, align='center', alpha=0.5)
plt.yticks(y_values1, objects1)
plt.xlabel('Estimated HIV prevalance value')
plt.ylabel('continent')
plt.title('Plot showing highest average HIV estimated prevalence of people aged 15 to 49 over the period 2000 to 2011')
plt.show()

df_subb2 = pd.DataFrame()
u_continent = df.continent.unique()
for i in u_continent:
    df_subb = df[df.continent == i]
    df_subb1 = df_subb[df_subb['mean_ind_val'] == df_subb['mean_ind_val'].min()]
    df_subb2 = df_subb2.append(df_subb1)
    
df_subb3 = df_subb2.groupby(['continent','mean_ind_val'])['country'].apply(lambda x: ','.join(x)).reset_index()
#print(df_subb3)

objects2 = list(df_subb3.continent)

y_values2 = np.arange(len(list(df_subb3.continent)))
x_values2 = list(df_subb3.mean_ind_val)
str12 = list(df_subb3.country)
str22 = list(round(df_subb3.mean_ind_val,2))

res2 = [i + ' - ' +  str(j) for i, j in zip(str12, str22)] 

for i in range(len(res2)): # your number of bars
    plt.text(x = x_values2[i], #takes your x values as horizontal positioning argument 
    y = y_values2[i], #takes your y values as vertical positioning argument 
    s = res2[i], # the labels you want to add to the data
    size = 9) # font size of datalabels


plt.barh(y_values2, x_values2, align='center', alpha=0.5)
plt.yticks(y_values2, objects2)
plt.xlabel('Estimated HIV prevalance value')
plt.ylabel('continent')
plt.title('Plot showing lowest average HIV estimated prevalence of people aged 15 to 49 over the period 2000 to 2011')
plt.show()

df_sub3 = df_sub3.sort_values(by=['continent'])
df_subb3 = df_subb3.sort_values(by=['continent'])


pd.concat({
    'One': df_sub3.set_index('continent').mean_ind_val, 
    'Two': df_subb3.set_index('continent').mean_ind_val
}, axis=1,sort=True).plot.bar()

plt.xlabel('continent')
plt.ylabel('Avg highest and lowest Value Level')
plt.title('Overlaid barchart of average highest and lowest estimated HIV prevalence indicators of people in each continent')
plt.show()

df_subbb2 = pd.DataFrame()
u_continent = df.continent.unique()
for i in u_continent:
    df_subbb = df[df.continent == i]
    df_subbb1 = df_subbb[df_subbb['mean_ind_val'] <= df_subbb['mean_ind_val'].mean()]
    df_subbb2 = df_subbb2.append(df_subbb1)
    
df_subz2 = pd.DataFrame()
for i in u_continent:
    df_subz = df_subbb2[df_subbb2.continent == i]
    df_subz1 = df_subz[df_subz['mean_ind_val'] == df_subz['mean_ind_val'].max()]
    df_subz2 = df_subz2.append(df_subz1)
    

df_subz2 = df_subz2.sort_values(by=['continent'])


m1_t = pd.DataFrame({
 'max_val' : list(round(df_sub3.mean_ind_val,2)),
 'min_val' : list(round(df_subb3.mean_ind_val,2))})

m1_t['max_val'].plot(kind='line',color='blue')
m1_t['min_val'].plot(kind='line',color='red')
plt.gca().legend(('max_val','min_val'))

ax = plt.gca()
plt.xlim([-0.35, len(m1_t['max_val'])-0.35])
ax.set_xticklabels(list(df_subz2.continent),rotation=45)
plt.title('Overlaid line chart for a country from each continent')
plt.show()


