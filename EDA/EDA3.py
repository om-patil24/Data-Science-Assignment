# -*- coding: utf-8 -*-


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/1-python/Assigment/advertising.csv")
df

df.shape
df.head
df.columns

df=df.rename(columns={'Daily_Time_ Spent _on_Site':'Daily time spent on site'})

# first movement : mean (central tendancy) give ave.measurement
mean_values = df.mean(numeric_only=True)
print('\n mean (First movement):\n',mean_values)


# Second movement business decission (Varience/ Standard deviation)
var_value = df.var(numeric_only=True)
print("\n second movement decission varience:\n",var_value) 

std_value = df.std(numeric_only=True)
print("Second movement Business Decission Standard deviation:\n",std_value)

# third movement business decission: skewnwss (symmetry)
skew_values = df.skew(numeric_only=True)
print('/nkskewness (Third movement):',skew_values)

# forth movement : kurtosis (peakedness)
kurt_values = df.kurt(numeric_only=True)
print('\nkurtosis (forth movement):\n', kurt_values)

# check the result
sns.histplot(df.Age,kde=True)
sns.histplot(df.Area_Income,kde=True)
sns.histplot(df.Male,kde=True )
sns.histplot(df.Timestamp,kde=True )

#Histogram of each column
df.drop(columns='Timestamp').hist(figsize=(10,8), color='skyblue',edgecolor='black')
plt.suptitle('Histogram of numerical feature')
plt.tight_layout()
plt.show()

'''# scatter plot :  sepal daimention
sns.scatterplot(data=df, x='Age', y='Area_Income')
plt.title('scatter plot: Age VS Area income')
plt.show() 
'''
sns.scatterplot(data=df, x='Area_Income', y='Age')
plt.title('scatter plot: Age VS Area income')
plt.show() 


sns.scatterplot(data=df, x='Age',y='Daily time spent on site')
plt.title("Scatter plot : Age VS Daili time spent on site")
plt.show()





