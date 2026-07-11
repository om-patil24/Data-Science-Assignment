# -*- coding: utf-8 -*-



import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,MinMaxScaler

df=pd.read_csv("C:/1-python/Assigment/crime_data.csv")
df

df.shape #(50, 5) row and columns
df.describe
df.describe()

df.isnull
df.isnull().sum()

df.fillna
df.shape

df=df.drop_duplicates # drop duplicate value
df

 # remove the duplicate rows

