from flask import Flask,json,request,jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)
loaded_model = pickle.load(open("model.pkl","rb"))
@app.route('/')
def start():
    return "WELCOME"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    arr = np.array(data)
    arr = arr.reshape(1,-1)
    predicted_data = loaded_model.predict(arr)
    print(predicted_data[0],"predicted data")
    return json_response({"response":predicted_data[0]})

def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})

