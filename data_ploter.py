import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

 
#Random
df_Data = pd.read_json(r'C:/Users/denev/TSP/Final_test')
df_Data["file"] = df_Data["file"].astype('category')
#dfSBST = pd.read_json(r'C:\Users\denev\.spyder-py3\BSTest4') 
#dfSBST ["Nazwa"] = dfSBST ["Nazwa"].astype('category')
#dfSBST ["SCMP"] = dfSBST .apply(lambda row: (row['Porownania'] / np.log2(row['Tablica'])), axis=1)
#dfSBST ["ST"] = dfSBST .apply(lambda row: (row['Czas'] / np.log2(row.Tablica)), axis=1)
#%%
df_Data["K"] = df_Data.apply(lambda row: 'sym' in row['file'] and 'asym' not in row['file'] and 'K' in row['function'],axis =1  )
tmp = df_Data.loc[df_Data['K'] == True]
#%%
df_Data["K"] = df_Data.apply(lambda row: 'sym' in row['file'] and 'asym' not in row['file'] and 'ENN' in row['function'],axis =1  )
tmp = df_Data.loc[df_Data['K'] == True]

#%%
df_Data["Comp"] = df_Data.apply(lambda row: 'sym' in row['file'] and 'asym' not in row['file'] ,axis =1  )
comp = df_Data.loc[df_Data['Comp'] == True]
#%%
df_Data["Comp2"] = df_Data.apply(lambda row: 'sym' in row['file'] and 'asym' not in row['file'] ,axis =1  )
comp = df_Data.loc[df_Data['Comp2'] == True]
#%%
sns.lineplot(data = tmp, x = 'file', y = 'time', hue = 'function')
#%%
sns.lineplot(data = comp, x = 'file', y = 'solution', hue = 'function')
#%%
sns.scatterplot(data = df_Data, x = 'function', y = 'solution', hue = 'file')
# %%
#sns.lineplot(data = dfSBST, x = 'Tablica', y = 'SCMP',hue = 'Nazwa')
# %%
df_Data = pd.read_json(r'C:/Users/denev/TSP/files3.json')
df_Data["file"] = df_Data["file"].astype('category')