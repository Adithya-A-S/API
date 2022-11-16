import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)




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
#@cross_origin()
def predict():
    payload = request.get_json(force=True)

    ls = list(payload.values())
    sm = sum(ls)
    if sm>260:
        prediction = 1
    else:
        prediction = 0
    
    output = {
        "data": {
            'prediction': prediction,
            'interpretation': 'have high chances of getting diabetes' if prediction == 1 else 'you are healthy!'
        }
    }
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)




