#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

if __name__ ==__main__:
   # Loading the dataset - both the traning set and the test set
    training_set=pd.read_csv('train.csv')
    testing_set=pd.read_csv('test.csv')

    # Preprocess the data
    def preprocess_data(df):
        df['Age'].fillna(df['Age'].median(),inplace=True)
        df['Embarked'].fillna(df['Embarked'].mode()[0],inplace=True)
        df['Fare'].fillna(df['Fare'].median(),inplace=True)
        df['Sex']=df['Sex'].map({'male':0,'female':1})
    
        return df
    training_df=preprocess_data(training_set)
    testing_df=preprocess_data(testing_set)

    # select desired features of the training
    features=['Pclass','Sex','Age','Fare']
    x=training_df[features]
    y=training_df['Survived']
    x_test=testing_df[features]

    # split training data
    x_train,x_val,y_train,y_val=train_test_split(x,y,test_size=0.2,random_state=42)

    # train a DecisionTreeClassifier
    dtc=DecisionTreeClassifier()
    dtc.fit(x_train,y_train)

    # evaluate the models accuracy
    y_pred=dtc.predict(x_val)
    accuracy=accuracy_score(y_val,y_pred)
    print(f"Validation Accuracy:{accuracy *100:.2f}%") 


