# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import  StandardScaler, MinMaxScaler

df=pd.read_csv("C:/1-python/Assigment/bank_data.csv")
df

df.shape # (45211, 32) rows and columns

df.columns # get the columns name 

df.isnull() # get the null vakues 

df.isnull().sum() # fill the null values 

df.describe # 

df.describe() # get the 5 number summery

df.dropna() # drop the null values

df2=df.drop_duplicates() # drop duplicate values
df2

df2_no_duplicates=df2.drop_duplicates() # remove the duplicate rows
df2

scaler_standard = StandardScaler()  #- StandardScaler: Transforms data so each feature has mean = 0 and standard deviation = 1.
 
df2_standard = scaler_standard.fit_transform(df2)
print("\nStandardized Data:\n",df2_standard)

#  Normalization (scaled between 0 and 1)
scaler_minmax = MinMaxScaler() #- MinMaxScaler: Scales features to a fixed range, usually [0, 1].

df2_minmax = scaler_minmax.fit_transform(df2)
print("\n Normalize data:\n",df2_minmax)
