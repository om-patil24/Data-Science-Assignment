# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:52:44 2025

@author: op372
"""

           'ASSIGMENT 5'
           
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/1-python/crime_data.csv')
df
df.describe
df.shape
# 50 rows and 5 colums

df.describe()

df=df.rename(columns={'unnames0':'Name'})
df.dtypes
##########FIRST MOVEMENT BUSINESS DECISSION #############
#MEAN WE FIND
mean_values=df.mean(numeric_only=True)
print('\nmean(First movement business decission)\n:',mean_values)


########## SECOND MOVEMENT BUSINESS DECISSION ########
#STANDARD 
#VARIENCE
std_value=df.std(numeric_only=True)
print('\nSTANDARD DEVIATION (second movement decission)\n:',std_value)
var_values=df.var(numeric_only=True)
print('\nVARIENCE (second movement decission)\n:',var_values)

######### THIRD MOVEMENT BUSINESS DECISSION ######
#SKEWNESS 
skew_values=df.skew(numeric_only=True)
print('\nSkewness (Thirs movement business decission)\n:',skew_values)

######## FORTH MOVEMENT BUSINESS DECISSION #######
#Kurtosis
kurt_values=df.kurt(numeric_only=True)
print('\nKurtosis (Third movement business decission)\n:',kurt_values)
sns.histplot(df.Murder,kde=True)
# we get the murder histogram graph which is right skewed

sns.histplot(df.Assault,kde=True)
# the graph is bymodel

sns.histplot(df.UrbanPop,kde=True,color='green')
# the UrbanPop data is left skewed

sns.histplot(df.Rape,kde=True,color='skyblue')
#the graph is right skewed

df.hist(figsize=(10,10),color='Green',edgecolor='black')
plt.subtitle("Crime rate graph")
plt.tight_layout()
plt.show()

############ Scatter plot #######################

sns.scatterplot(data=df,x='Rape',y='Murder',color='skyblue')
plt.show()