import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)




@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return {"data": "Welcome to online diabetes prediction model"}

