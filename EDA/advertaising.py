                              'EDA'

import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# we create the data frame 

df=pd.read_csv('C:/1-python/advertising.csv')
df.info()

                            'Rename the columns '
                            
df=df.rename(columns = {'Daily_Time_ Spent _on_Site':'Dily time spent', 'Area_Income':'total income','Daily Internet Usage':'internet use','Clicked_on_Ad':'Clicked Ad'})
df.dtypes
df.shape
df.size
df.info()
df.T
df['Age']
df.describe()

'daily time is left skewed data'
'Age is slighly right skewd'
'Male is right skewed'
'Clicked Ad is perfectly symmetric '



#################### first movement business decission  ###################

# WE FIND THE MEAN AND CENTRAL TENDENCEY
mean_values = df.mean(numeric_only=True)
print('\n mean (First movement):\n',mean_values)

#################### SECOND MOVEMENT BUSINESS DECISSION ##################

# ITS VARIENCE AND STANDARD DEVIATION
var_values = df.var(numeric_only=True)
std_values = df.std(numeric_only=True)
print('\nvarience (second movement):\n',var_values)
print('\nstandard (second movement):\n',std_values)



##################### THIRS MOVEMENT BUSINESS DECISION ####################

# SKEWNWSS
skew_values = df.skew(numeric_only=True)
print('\nskewnwss (thirs movement):\n',skew_values)

#'daily time spent , total income and ,internet use are left skew'
#'age , male  and ,clicked Ad are symmetric'

################### FORTH MOVEMENT BUSINESS DECISION ####################

# KERTOSIS
kurt_values = df.kurtosis(numeric_only=True)
print('n\kurtosis (thirs movement):\n',kurt_values)

# we check the result
# we check the skewness
sns.histplot(df.Age,kde=True)
#'data is slightly right skewed median is near to age30'

sns.histplot(df['total income'],kde=True)
#'total income is left skewed mean salary is 60000'

sns.histplot(df['internet use'],kde=True)
df['internet use'].describe()
#'mean is less then median data is left skewed'
#'its graph is bimodel'

sns.histplot(df['Male'],kde=True)
df['Male'].describe()
#'its slighly right skewed'
#'the graph is bimodel'

sns.histplot(df['Clicked Ad'], kde=True)
df['Clicked Ad'].describe()
#'the clicked ad is symmetric '
#'the graph is bimodel'
################ VISUAL EXPLORATION ###########################

# USE HISTOGRAM FOR EACH COLUMN
df.drop(columns='Age').hist(figsize=(10,8), color= 'skyblue',edgecolor='black')
plt.suptitle('hist for numeric feature')
plt.tight_layout()
plt.show()

############## BY USING THE FOR LOOP ###################

a=df.select_dtypes(include='number').columns.tolist()
for i,var in enumerate(a):
    plt.subplot(3,2,i+1)
    sns.histplot(df[var])

################## SCATTER PLOT ###########################

sns.scatterplot(data=df, x='Age', y='total income')
plt.title('total income with age')
plt.show()
#'no relation between age and total income