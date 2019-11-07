from flask import Flask, make_response, request, jsonify, render_template
from pythainlp import word_tokenize

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

@app.route("/webhook", methods=['POST'])
def webhook():
    # return response()
    req = request.get_json(force=True)
    event = req.get('queryResult').get('parameters').get('Event')
    sex = req.get('queryResult').get('parameters').get('Sex')
    relationship = req.get('queryResult').get('parameters').get('Relationship')
    age = req.get('queryResult').get('parameters').get('Age')
    price = req.get('queryResult').get('parameters').get('Price')
    # if event == 'วาเลนไทน์':
    #     event = 0
    # elif event == 'ปีใหม่':
    #     event = 1
    # else :
    #     event = 2
    # if sex == 'ชาย':
    #     sex = 0
    # elif sex == 'หญิง':
    #     sex = 1
    # else:
    #     sex = 0
    # if relationship == 'ครอบครัว':
    #     relationship = 0
    # elif relationship == 'เพื่อน':
    #     relationship = 1
    # else:
    #     relationship = 2
    # if age == 'วัยรุ่น':
    #     age = 0
    # elif age == 'ผู้ใหญ่':
    #     age = 1
    # else:
    #     age = 2
    result = {} # an empty dictionary
    result["fulfillmentText"] = relationship
    result = jsonify(result)
    return make_response(result)# return the result json
if __name__ == "__main__":
    app.run()