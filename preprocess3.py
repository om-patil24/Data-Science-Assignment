# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("C:/1-python/Assigment/Company_Data.csv")
df

df.shape

df.info

df.describe

df.describe() # 5 number summery

df.isnull

df.isnull().sum()

df=df.drop_duplicates()
df

df_no_duplicates=df.drop_duplicates() # remove the duplicate rows
df

