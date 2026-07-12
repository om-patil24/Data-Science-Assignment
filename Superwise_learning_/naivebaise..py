# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:58:45 2026

@author: op372
"""
"    Naive Bayes is a Classification algorithm"
        'Simple gaussian'
        
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# load the data set
df = pd.read_csv("C:/1-python/Assigment/advertising.csv")
df

df.shape  #(1000, 10) row and columns

df.head   # first five rows

df.describe

df.describe() # get the five number summery 

# prepocess the data 

df.isnull
 
df.isnull().sum()  # no  ull value

# check how many duplicate rows
df[df.duplicated()]


df2=df.drop_duplicates()
df2.shape

# removing the unwanted columns 
"""  'Ad_Topic_Line','City','Country','Timestamp'  """
df2 = df2.drop(columns=['Ad_Topic_Line','City','Country','Timestamp'])

#  Correlation Matrix (Only Numeric Columns)
print(df2.corr(numeric_only=True))

print(df2.columns) # check the columns name

print(type(df2))  
 
       'plot the graph'
       
df=df.hist(figsize=(8,6))
plt.show()

       'Correlation Hit-Map'
       
plt.figure(figsize=(10,9))
sns.heatmap(df2.corr(numeric_only=True), annot = True, cmap="coolwarm")
plt.show()

'''
1. Daily_Time_Spent_on_Site vs Clicked_on_Ad = -0.75
Strong negative correlation.
Users who spend more time on the website are less likely to click the ad.

2. Daily Internet Usage vs Clicked_on_Ad = -0.79
Strong negative correlation.
Users with higher internet usage are less likely to click the ad.

3. Age vs Clicked_on_Ad = 0.49
Moderate positive correlation.
Older users are more likely to click the ad.

4. Area_Income vs Clicked_on_Ad = -0.48
Moderate negative correlation.
Users with higher income are less likely to click the ad.

5. Male vs Clicked_on_Ad = -0.038
Very weak correlation (almost 0).
Gender has almost no effect on whether the user clicks the ad.
'''


            'Count plot'
            
sns.countplot(data=df2, x='Clicked_on_Ad')  #0 = User did not click the advertisement.
                                                #1 = User clicked the advertisement
plt.show()

# create the new columns with lable 
df2['Ad_Click_Status'] = df2['Clicked_on_Ad'].map({
    0: "Not Clicked",
    1: "Clicked"
})


sns.countplot(data=df2, x='Ad_Click_Status')
plt.title("Advertisement Click Distribution")
plt.xlabel("Ad Click Status")
plt.ylabel("Count")
plt.show()


            'Box plot'
        
sns.boxplot(data=df2[['Age','Area_Income']])
plt.show()

            'Pair plot'
            
sns.pairplot(data=df2, hue='Clicked_on_Ad')
plt.show()


# Saperate the feature and target 
x = df2.drop("Clicked_on_Ad",axis=1)
y = df2['Clicked_on_Ad']

# split the data into training and testing 

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

df2['Ad_Click_Status'] = df2['Clicked_on_Ad'].map({
    0: "Not Clicked",
    1: "Clicked"
})

sns.countplot(data=df2, x='Ad_Click_Status')
plt.title("0 = not clicked and 1 = clicked")
plt.show()


x = df2.drop("Clicked_on_Ad",axis=1)
y = df2['Clicked_on_Ad']

#If you've already replaced Clicked_on_Ad with strings, convert it back:
    
df2['Clicked_on_Ad'] = df2['Clicked_on_Ad'].map({
    'Not Clicked': 0,
    'Clicked': 1
})

# Train the Naive Bayes moel
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(x_train, y_train)

print(x_train.head())
print(y_train.head())

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy",accuracy)

############################################################

print("x_train shape:", x_train.shape)
print('x_test score:',x_test.shape)
print("y_train Shape :", y_train.shape)
print("y_test Shape  :", y_test.shape)


# for calculate the accuracy 
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy =", accuracy)
print("Accuracy Percentage =", accuracy * 100)

# Confussion matrics
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# classification report 
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))


# confussion matrics and classification report 

'prediction '
y_pred = model.predict(x_test)
#print(y_pred)

'Accuracy'
accuracy = accuracy_score(y_test, y_pred)
print('accuracy:',accuracy)

'Confussion matrics '
print("\nConfussion Matrics")
print(confusion_matrix(y_test, y_pred))

 'lassification Report'
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
