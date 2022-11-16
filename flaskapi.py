import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)

model = pickle.load(open('./model.pkl', 'rb'))


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return {"data": "Welcome to online diabetes prediction model"}
@app.route('/welcome', methods=['GET'])
@cross_origin()
def homepage():

    return """
    <h1>Diabetes Prediction API</h1>
    <p1>By Adithya A S</p1>
    <img src="https://media.giphy.com/media/J1RWP1OyfkwATrL9cd/giphy.gif"/>
    """

@app.route('/prediction', methods=['POST'])
@cross_origin()
def predict():
    payload = request.get_json(force=True)
    prediction = model.predict([np.array(list(payload.values())+[0.3])]).tolist()[0]

    output = {
        "data": {
            'prediction': prediction,
            'interpretation': 'have high chances of getting diabetes' if prediction == 1 else 'you are healthy!'
        }
    }
    return jsonify(output)


