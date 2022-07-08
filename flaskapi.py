import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)

model = pickle.load(open('./model.pkl', 'rb'))


@app.route('/welcome')
@cross_origin()
def home():
    return {"data": "Welcome to online diabetes prediction model"}
@app.route('/')
@cross_origin()
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

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



if __name__ == "__main__":
    app.run(debug=True)