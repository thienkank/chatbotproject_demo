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
with open(f'model/gift_model_xgboost.pkl', 'rb') as f:
    model = pickle.load(f)
input=pd.DataFrame([[1, 0, 0, 0]],columns=['event','relationship','sex','age'])
prediction = model.predict(input)[0]
if prediction == 0:
    prediction = "เสื้อผ้าผู้ชาย"
elif prediction == 1:
    prediction = "รองเท้าผู้ชาย"
elif prediction == 2:
    prediction = "กระเป๋าผู้ชาย"
elif prediction == 3:
    prediction = "นาฬิกาผู้ชาย"
elif prediction == 4:
    prediction = "แว่นตาผู้ชาย"
elif prediction == 5:
    prediction = "น้ำหอมผู้ชาย"
elif prediction == 6:
    prediction = "เครื่องสำอางผู้ชาย"
elif prediction == 7:
    prediction = "เครื่องประดับผู้ชาย"
elif prediction == 8:
    prediction = "กีฬาผู้ชาย"
elif prediction == 9:
    prediction = "เสื้อผ้าผู้หญิง"
elif prediction == 10:
    prediction = "รองเท้าผู้หญิง"
elif prediction == 11:
    prediction = "กระเป๋าผู้หญิง"
elif prediction == 12:
    prediction = "นาฬิกาผู้หญิง"
elif prediction == 13:
    prediction = "แว่นตาผู้หญิง"
elif prediction == 14:
    prediction = "น้ำหอมผู้หญิง"
elif prediction == 15:
    prediction = "เครื่องสำอางผู้หญิง"
elif prediction == 16:
    prediction = "เครื่องประดับผู้หญิง"
elif prediction == 17:
    prediction = "กีฬาผู้หญิง"
elif prediction == 18:
    prediction = "อุปกรณ์อิเล็กทรอนิกส์"
elif prediction == 19:
    prediction = "กล้อง"
elif prediction == 20:
    prediction = "อุปกรณ์ฟิตเนส"
else :
    prediction = "อาหารสุขภาพ"
print ("คำตอบคือ ",prediction)