import numpy as np
from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin

app = Flask(__name__)




@app.route('/welcome', methods=['GET'])
@cross_origin()
def home():
    return {"data": "Welcome to online diabetes prediction model"}
@app.route('/', methods=['GET'])
@cross_origin()
def homepage():

    return """
    <h1>Diabetes Prediction API</h1>
    <p1>By Adithya A S</p1>
    <img src="https://media.giphy.com/media/J1RWP1OyfkwATrL9cd/giphy.gif"/>
    """





if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)