# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load the data set 
df = pd.read_csv("C:/1-python/Assigment/advertising.csv")
df

#information of the data set
df.info

# how many row and columns are present
# (1000, 10)
df.shape

# Give the 5 number summery
df.describe ()

df.isnull().sum() # no null or missing value are present 

df.columns # check the columns name 

df.dropna() # remove the missing value

df=df.drop_duplicates() # remove the duplicaye value

df.drop_duplicates

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

scaler_standard = StandardScaler() # Transforms data so each feature has mean = 0 and standard deviation = 1.
df_standard= scaler_standard.fit_transform(df)
print("\n Standaraization:\n",df_standard)

#  Normalization (scaled between 0 and 1)
scaler_minmax = MinMaxScaler() #MinMaxScaler: Scales features to a fixed range, usually [0, 1].
df_minmax = scaler_minmax.fit_transform(df)
print("\n Normalaization:\n",df_minmax)


