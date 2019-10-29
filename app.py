from flask import Flask, make_response, request, jsonify, render_template
from pythainlp import word_tokenize

app = Flask(__name__)

# def tokenize(sentence):
#     words=word_tokenize(sentence, engine='pylexto')
#     tokens="|".join(str(i) for i in words)
#     return tokens

# def response():# definition of the results function
    # req = request.get_json(force=True)
    # sentence = req.get('queryResult').get('queryText')
    # result = {} # an empty dictionary
    # result["fulfillmentText"] = tokenize(sentence)
    # result = jsonify(result)
    # return make_response(result)# return the result json

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=['GET','POST'])
def webhook():
    # return response()
    fulfillmentMessages = {} # an empty dictionary
    fulfillmentMessages["fulfillmentText" : "ปกติ"]
    fulfillmentMessages = jsonify(result)
    return make_response(result)# return the result json

if __name__ == "__main__":
    app.run()