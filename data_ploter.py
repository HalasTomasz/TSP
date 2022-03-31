import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

 
#Random
df_Data = pd.read_json(r'C:/Users/denev/TSP/test4')
df_Data["file"] = df_Data["file"].astype('category')
 
#dfSBST = pd.read_json(r'C:\Users\denev\.spyder-py3\BSTest4') 
#dfSBST ["Nazwa"] = dfSBST ["Nazwa"].astype('category')
#dfSBST ["SCMP"] = dfSBST .apply(lambda row: (row['Porownania'] / np.log2(row['Tablica'])), axis=1)
#dfSBST ["ST"] = dfSBST .apply(lambda row: (row['Czas'] / np.log2(row.Tablica)), axis=1)

 

#%%
sns.barplot(data = df_Data, x = 'function', y = 'time', hue = 'file')
#%%
sns.scatterplot(data = df_Data, x = 'function', y = 'time', hue = 'file')
#%%
sns.scatterplot(data = df_Data, x = 'function', y = 'solution', hue = 'file')
# %%
#sns.lineplot(data = dfSBST, x = 'Tablica', y = 'SCMP',hue = 'Nazwa')
# %%
#sns.lineplot(data = dfSBST, x = 'Tablica', y = 'Czas', hue = 'Nazwa')