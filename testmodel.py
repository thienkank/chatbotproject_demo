# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/thienkank/chatbotproject/master/dataset/dataset.csv',names=['event','relationship','sex','age','description','class'])

import xgboost as xgb
from sklearn.model_selection import train_test_split
x = data[['event', 'relationship', 'sex', 'age']]
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=59)
classifier = xgb.sklearn.XGBClassifier(nthread=-1, seed=1)
classifier.fit(X_train, y_train)

import pickle
with open('gift_model_xgboost.pkl', 'wb') as file:
    pickle.dump(classifier, file)
    print("Build model success!")