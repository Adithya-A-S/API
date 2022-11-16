import pickle

import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

model = pickle.load(open('./model.pkl', 'rb'))



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




