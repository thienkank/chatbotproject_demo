from flask import Flask, make_response, request, jsonify, render_template
# from pythainlp import word_tokenize

import pandas as pd
import pickle

app = Flask(__name__)

# def tokenize(sentence):
#     words=word_tokenize(sentence, engine='pylexto')
#     tokens="|".join(str(i) for i in words)
#     return tokens

# def response():# definition of the results function
#     req = request.get_json(force=True)
#     sentence = req.get('queryResult').get('queryText')
#     result = {} # an empty dictionary
#     result["fulfillmentText"] = tokenize(sentence)
#     result = jsonify(result)
#     return make_response(result)# return the result json

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=['GET','POST'])
def webhook():
    # return response()
    req = request.get_json(force=True)
    event = req.get('queryResult').get('parameters').get('Event')
    sex = req.get('queryResult').get('parameters').get('Sex')
    relationship = req.get('queryResult').get('parameters').get('Relationship')
    age = req.get('queryResult').get('parameters').get('Age')
    price = req.get('queryResult').get('parameters').get('Price')
    if event == 'วาเลนไทน์':
        event = 0
    elif event == 'ปีใหม่':
        event = 1
    else :
        event = 2
    if sex == 'ชาย':
        sex = 0
    elif sex == 'หญิง':
        sex = 1
    else:
        sex = 0
    if relationship == 'ครอบครัว':
        relationship = 0
    elif relationship == 'เพื่อน':
        relationship = 1
    else:
        relationship = 2
    if age == 'วัยรุ่น':
        age = 0
    elif age == 'ผู้ใหญ่':
        age = 1
    else:
        age = 2
    with open(f'model/gift_model_xgboost.pkl', 'rb') as f:
        model = pickle.load(f)
    input=pd.DataFrame([['event', 'relationship', 'sex', 'age']],columns=['event','relationship','sex','age','description','class'])
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
    #response=str(event)+" "+str(sex)+" "+str(relationship)+" "+str(age)
    result = {} # an empty dictionary
    result["fulfillmentText"] = prediction
    result = jsonify(result)
    return make_response(result)# return the result json
if __name__ == "__main__":
    app.run()