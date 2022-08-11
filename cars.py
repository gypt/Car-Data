
# coding: utf-8

# In[9]:


import pandas as p
import matplotlib.pyplot as mpl
k = 0
m = 1
def best(x):
    print('FASTEST ACCELERATION: ', '19' + str(x.loc[x['Power/Weight'] == x['Power/Weight'].max()].iloc[0, 6]),
    x.loc[x['Power/Weight'] == x['Power/Weight'].max()].iloc[0, 0], '(' + 
    str(x.loc[x['Power/Weight'] == x['Power/Weight'].max()].iloc[0, 7]) + ')', '\n\nHIGHEST QUALITY ENGINE: ', 
    '19' + str(x.loc[x['Engine_Qual'] == x['Engine_Qual'].max()].iloc[0, 6]),
    x.loc[x['Engine_Qual'] == x['Engine_Qual'].max()].iloc[0, 0], '(' + 
    str(x.loc[x['Engine_Qual'] == x['Engine_Qual'].max()].iloc[0, 7]) + ')', '\n\nHIGHEST RPM: ',
    '19' + str(x.loc[x['rpm index'] == x['rpm index'].max()].iloc[0, 6]),
    x.loc[x['rpm index'] == x['rpm index'].max()].iloc[0, 0], '(' + 
    str(x.loc[x['rpm index'] == x['rpm index'].max()].iloc[0, 7]) + ')', '\n\nBEST OVERALL: ',
    '19' + str(x.loc[x['Value'] == x['Value'].max()].iloc[0, 6]),
    x.loc[x['Value'] == x['Value'].max()].iloc[0, 0], '(' + str(x.loc[x['Value'] == x['Value'].max()].iloc[0, 7]) + ')')    
def plot(x):
    mpl.figure(1)
    x.groupby('Origin')['Engine_Qual'].mean().plot(kind = 'bar')
    mpl.xlabel('Country')
    mpl.ylabel('Engine Quality')
    mpl.suptitle("Average Engine Quality by Country")
    mpl.savefig('EngineQualBar.png')
    mpl.figure(2)
    x.groupby('Year')['Engine_Qual'].mean().plot(kind = 'line')
    mpl.xlabel('Year')
    mpl.ylabel('Engine Quality')
    mpl.suptitle("Average Engine Quality by Year")
    mpl.savefig('EngineQualLine.png')     
def sort(x): #x['column_name'].describe() was used to determine quartile values
    x.loc[(x['Power/Weight'] >= 3.81), 'Acceleration'] = 'Very Good' 
    x.loc[(x['Power/Weight'] >= 3.43) & (x['Power/Weight'] <= 3.81), 'Acceleration'] = 'Good'
    x.loc[(x['Power/Weight'] >= 3.08) & (x['Power/Weight'] <= 3.43), 'Acceleration'] = 'Average'
    x.loc[(x['Power/Weight'] <= 3.08), 'Acceleration'] = 'Poor'
    x.loc[(x['HP/Liter'] >= 44.93), 'Power/Engine Volume'] = 'Very Good'
    x.loc[(x['HP/Liter'] >= 36.37) & (x['HP/Liter'] <= 44.93), 'Power/Engine Volume'] = 'Good'
    x.loc[(x['HP/Liter'] >= 27.98) & (x['HP/Liter'] <= 36.37), 'Power/Engine Volume'] = 'Average'
    x.loc[(x['HP/Liter'] <= 27.98), 'Power/Engine Volume'] = 'Poor'
    x.loc[(x['rpm index'] >= 8.33), 'Rev/Min(RPM)'] = 'Very Good'
    x.loc[(x['rpm index'] >= 6.23) & (x['rpm index'] <= 8.33), 'Rev/Min(RPM)'] = 'Good'
    x.loc[(x['rpm index'] >= 5.18) & (x['rpm index'] <= 6.23), 'Rev/Min(RPM)'] = 'Average'
    x.loc[(x['rpm index'] <= 5.18), 'Rev/Min(RPM)'] = 'Poor'
    x.loc[(x['Engine_Qual'] >= 132.22), 'Engine Integrity'] = 'Very Good'
    x.loc[(x['Engine_Qual'] >= 88.82) & (x['Engine_Qual'] <= 132.22), 'Engine Integrity'] = 'Good'
    x.loc[(x['Engine_Qual'] >= 46.02) & (x['Engine_Qual'] <= 88.82), 'Engine Integrity'] = 'Average'
    x.loc[(x['Engine_Qual'] <= 46.02), 'Engine Integrity'] = 'Poor'
    x.loc[(x['Value'] >= 209.45), 'Overall Grade'] = 'A'
    x.loc[(x['Value'] >= 104.45) & (x['Value'] <= 209.45), 'Overall Grade'] = 'B'
    x.loc[(x['Value'] >= 44.40) & (x['Value'] <= 104.45), 'Overall Grade'] = 'C'
    x.loc[(x['Value'] <= 44.40), 'Overall Grade'] = 'D'
    x.drop(['Power/Weight', 'HP/Liter', 'rpm index', 'Engine_Qual', 'Displacement',
           'MPG', 'Cylinders', 'Brake HP', 'Weight'], axis = 1, inplace = True)
    return x.head(50)

x = p.read_csv('carsdata.csv') 
x.set_index('Index', inplace = True)
x['Engine Volume (L)'] = (x['Displacement'] / 61.02).apply(lambda x: round(x, m))
x['Power/Weight'] = (x['Brake HP'] / x['Weight']) * 100
x['HP/Liter'] = (x['Brake HP'] / x['Engine Volume (L)'])
x['rpm index'] = (x['Cylinders'] / x['Engine Volume (L)']) * x['Power/Weight']
x['Engine_Qual'] = (x['HP/Liter'] * x['MPG']) / 10
x['Value'] = ((x['Engine_Qual'] * x['HP/Liter'] * x['Power/Weight']) / 100).apply(lambda x: round(x, k)) 
best(x)
plot(x)
sort(x)
#print(x)

