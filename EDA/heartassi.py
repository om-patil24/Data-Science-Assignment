# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 17:52:22 2025

@author: op372
"""

                             'ASSIGMENT 4'
                             
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/1-python/heart disease.csv')
df
df.shape
# 303 COLUMNS AND 14 ROWS

df.describe
df.describe()

'''age         sex          cp  ...          ca        thal      target
count  303.000000  303.000000  303.000000  ...  303.000000  303.000000  303.000000
mean    54.366337    0.683168    0.966997  ...    0.729373    2.313531    0.544554
std      9.082101    0.466011    1.032052  ...    1.022606    0.612277    0.498835
min     29.000000    0.000000    0.000000  ...    0.000000    0.000000    0.000000
25%     47.500000    0.000000    0.000000  ...    0.000000    2.000000    0.000000
50%     55.000000    1.000000    1.000000  ...    0.000000    2.000000    1.000000
75%     61.000000    1.000000    2.000000  ...    1.000000    3.000000    1.000000
max     77.000000    1.000000    3.000000  ...    4.000000    3.000000    1.000000'''

##################### FIRST MOVEMENT BUSINESS DECISSION #################

mean_values=df.mean(numeric_only=True)
print("\nmean (first movement business decission):",mean_values)

'''
mean (first movement business decission): age          54.366337
sex           0.683168
cp            0.966997
trestbps    131.623762
chol        246.264026
fbs           0.148515
restecg       0.528053
thalach     149.646865
exang         0.326733
oldpeak       1.039604
slope         1.399340
ca            0.729373
thal          2.313531
target        0.544554
dtype: float64'''


##################### SECOND MOVEMENT BUSSINESS DECISSION ###################

#VARIENCE
#STANDARD DEVIATION

var_values= df.var(numeric_only=True)
print("\nvarience (second movement business decission) :", var_values)

'''varience (second movement business decission) : age           82.484558
sex            0.217166
cp             1.065132
trestbps     307.586453
chol        2686.426748
fbs            0.126877
restecg        0.276528
thalach      524.646406
exang          0.220707
oldpeak        1.348095
slope          0.379735
ca             1.045724
thal           0.374883
target         0.248836
dtype: float64'''

std_values= df.std(numeric_only=True)
print("\nstandard deviation (second movement business decission):", std_values)
# Chol is high standard value is more affordable for feature engineer

''' standard deviation (second movement business decission): age          9.082101
sex          0.466011
cp           1.032052
trestbps    17.538143
chol        51.830751
fbs          0.356198
restecg      0.525860
thalach     22.905161
exang        0.469794
oldpeak      1.161075
slope        0.616226
ca           1.022606
thal         0.612277
target       0.498835
dtype: float64'''

################# THIRD MOVEMENT BUSINESS DECISSION #################


# KURTOSIS
kurt_values = df.kurt(numeric_only=True)
print("\nkurtosis (third movement business decission):",kurt_values)
# chol is high pickedness value and other are symmetric
################# FORTH MOVEMENT BUSINESS DECISSION ################

#SKEWNESS

skew_values = df.skew(numeric_only=True)
print("\nSKEWNESS (second movement business decisssion):",skew_values)
# the maximum value are near the 0 means it semmetric (bell shape curve)

############ VISUAL EXPLORATION ######################
df.drop(columns='age').hist(figsize=(10,8), color='green',edgecolor='black')
plt.subtitle("VISUALIATION OF HEARD DECISEACE")
plt.tight_layout()
plt.show()


############ SCATTER PLOT ###########################
sns.scatterplot(data=df,x='age',y='sex')
plt.title("heart disease data")
plt.show()








