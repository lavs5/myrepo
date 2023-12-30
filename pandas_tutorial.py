import os
import pandas as pd
import seaborn as sns

f=r"C:\MyGISstuff\py\liv_pop.csv"
df=pd.read_csv(f,index_col="GeographyCode")
# print(f)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.describe().T)
# print(df.min())
# print(df.max())
# print(df['Africa'].min())
# print

total=df.sum(axis=1)

df['Total']=total
print(df.head())