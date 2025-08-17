# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 18:01:52 2025

@author: op372
"""

                 ''
                 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('C:/1-python/EastWestAirlines.xlsx')
df

df.shape
#(3999, 12) their are 3999 row and 12 column

df.describe
df.describe()
# we get the 5 number summery 
'''ID#  Balance  Qual_miles  ...  Flight_trans_12  Days_since_enroll  Award?
0        1    28143           0  ...                0               7000       0
1        2    19244           0  ...                0               6968       0
2        3    41354           0  ...                0               7034       0
3        4    14776           0  ...                0               6952       0
4        5    97752           0  ...                4               6935       1
   ...      ...         ...  ...              ...                ...     ...
3994  4017    18476           0  ...                1               1403       1
3995  4018    64385           0  ...                0               1395       1
3996  4019    73597           0  ...                0               1402       1
3997  4020    54899           0  ...                1               1401       0
3998  4021     3016           0  ...                0               1398       0

[3999 rows x 12 columns]'''

################### FIRST MOVEMENT BUSINESS DECISION ###########

mean_values = df.mean(numeric_only=True)
print('\nmean (first movement business decission)\n:', mean_values)
# we get the mean 
# award mean is 0 means its symmetric 
# the othge mean are 1 or more than 1 then it is not symmertic 
################## SECOND MOVEMENT BUSINESS DECISSION ########
var_values = df.var(numeric_only=True)
std_values = df.std(numeric_only=True)
print('\nvarience (second movement bisiness decission)\n:', var_values)
print('\nstandard (second movement business decission)\n:', std_values)
# the varience and standard deviation are not the near of zero 
# Bonus_trans = 9.223317e+01 it will contribute more in feature engineer
################# THIRD MOVEMENT BUSINESS DECISSION #########
# KURTOSIS
kurt_values = df.kurt(numeric_only=True)
print('\nkurtosis (third movement business decission)\n:',kurt_values)

#  the kurtosis is means high pickedness 

############### FORTH MOVEMENT BUSINESS DECISSION ##########
# SKWENESS
skew_values = df.skew(numeric_only = True)
print('\nskewness (third movement business decission)\n:',skew_values)
# Award and days_since_enroll are 0 means it symmetric 
# all are more than 0 and positive means they all are positive 
############ VISUAL EXPLORATION ################

df.drop(columns='ID#').hist(figsize=(20,20),color='green',edgecolor='black')
plt.subtitle('East weast data')
plt.tight_layout()
plt.show()
# Days_since_enroll, Award,cc1_miles are bymodel and rest of all are right skewed 
############ BY USING THE FOR LOOP #####################

a = df.select_dtypes(inclide='number').coloums.tolist()
for i, var in enumerate(a):
    plt.subplot(3,2,i+1)
    sns.histplot(df[var], kde=True)
    
########### scatter plot #############
sns.scatterplot(data=df, x='Balance',y='Award?')
plt.title('Balance And Award analysyis ')
plt.show()
# their is no relation between balance and reward
    
    


















