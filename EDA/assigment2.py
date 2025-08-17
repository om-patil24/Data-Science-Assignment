# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 09:13:06 2025

@author: op372
"""
              'ASSIGMENT 2 BANK DATA'
        
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('bank_data.csv')  
df                   
'age  default  balance  housing  ...  jotechnician  jounemployed  jounknown  y
0       58        0     2143        1  ...             0             0          0  0
1       44        0       29        1  ...             1             0          0  0
2       33        0        2        1  ...             0             0          0  0
3       47        0     1506        1  ...             0             0          0  0
4       33        0        1        0  ...             0             0          1  0
   ...      ...      ...      ...  ...           ...           ...        ... ..
45206   51        0      825        0  ...             1             0          0  1
45207   71        0     1729        0  ...             0             0          0  1
45208   72        0     5715        0  ...             0             0          0  1
45209   57        0      668        0  ...             0             0          0  0
45210   37        0     2971        0  ...             0             0          0  0

'[45211 rows x 32 columns]'



df=df.rename(columns = {'jotechnician':'jcn','jounemployed ':'jpd','jounknown':'jn'})
# we rename the column

df.dtypes
# it gives the all values

df.shape
#(45211 ROWS , 32 COLUMNS)

df.describe()
# we get the 5 number summery 
# mean of age is greater then the median 
# mean of default is greater then the median
# mean of jn is greater then the median 
# mean of y is greater then the median

 
############## FIRST MOVEMENT BUSINESS DECISSION ################
mean_values = df.mean(numeric_only=True)
print('\nmean(first bussiness decision)\n:',mean_values)

median_values = df.median(numeric_only=True)
print('\nmedian\n:',median_values)  
         
############## SECOND MOVEMENT BUSINESS DECISION ##################

# WE FIND STANDAERD AND VARIENCE VALUE
var_values = df.var(numeric_only=True)
std_values = df.std(numeric_only=True)
print('\nvarience (second business decission)\n:',var_values)
print('\nstandard (second movement decission)\n', std_values)
# the variable having high standard deviation so we can select it for model building
# the variable having loe standard deviation so we reject the value 


################ SKEWNESS ###############
skew_values = df.skew(numeric_only=True)
print('\nskewness (third movement bisiness decission)\n:',skew_values)
# the value is greater than the zero then its right skewed
# the value is less than the zero the its right skewed
# the value is perfectly 0 or .0.1 then its symmetric

################ kurtosis ################
kurt_values = df.kurt(numeric_only=True)
print('\nkurtosis(forth business decision\n:',kurt_values)
# the value is high outlier is more 
# the value is low outlier is less


############## VISUAL EXPLORATION #######
#USE HISTOGRAM FOR EACH COLUMN
df.drop(columns='balance').hist(figsize=(20,20), color='green',edgecolor='white')
plt.subtitle('bank data visualization')
plt.tight_layout()
plt.show()


############ BY USING THE FOR LOOP ######### ITS NOTN NECESSARY 
a=df.select_dtypes(include='number').columns.tolist()
for i,var in enumerate(a):
    plt.subplot(3,2,i+1)
    sns.histplot(df[var],kde=True)
    
    

########### SCATTER PLOT ############
sns.scatterplot(data=df, x='age',y='balance')
plt.title('bank management')
plt.show()   #  THEIR ARE NO RELATIONSHIP BETWEEN BALANCE AND AGE
