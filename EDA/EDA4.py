# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:50:11 2026

@author: op372
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv("C:/1-python/Assigment/heart disease.csv")
df

df.shape  # get the number of rows ans columns (303, 14)
df.describe

df.describe() # we get the five number summery 

df.columns # we get the columns name 

# first movement business decission we find out the mean(central tendency) it gives the Average measure 
mean_values = df.mean(numeric_only=True)
print("\n First movement Business Decission{mean}:\n",mean_values)

# Second movement business decission (Varience \ Standard Deviation)

var_values = df.var(numeric_only=True)
print("\n Second movement Decission {varience}:\n",var_values)

std_values = df.std(numeric_only=True)
print("\n second movement decission {standard deviation}\n",std_values)

# Third movement business decission Skewness
skew_values = df.skew(numeric_only=True)
print("\n Third movement decission {Skewness}:\n",skew_values)

# Forth movement business decission Kurtosis
kurt_values = df.kurt(numeric_only=True)
print("\n Third movement decission {Kurtosis}:\n",kurt_values)

'''    VISUALIZE THE GRAPH    '''


# CHECK THE RESULT 
sns.histplot(df.oldpeak,kde=True) # data is right skew
sns.histplot(df.age)

# use histogrm for vidsualization 

df.hist(figsize=(15,8),color='green',edgecolor='white')
plt.title("Histogram Visualization")
plt.tight_layout()
plt.show()


# scatter plot
sns.scatterplot(data=df,x='age',y='thalach')
plt.title("Realation Between {Age VS Thalach}")
plt.show()


'''plt.pie(x=[15, 8], labels=['age', 'thalach'], colors=['green', 'blue'],
        autopct='%1.1f%%', shadow=True, startangle=140)
'''