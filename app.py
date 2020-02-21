from flask import Flask,json,request,jsonify
from flask_cors import CORS
import numpy as np
from sklearn import datasets, linear_model, metrics 
import pickle

app = Flask(__name__)
CORS(app)

boston = datasets.load_boston(return_X_y=False) 
X = boston.data 
y = boston.target 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,  random_state=1) 
reg = linear_model.LinearRegression() 
reg.fit(X_train, y_train) 
print('Coefficients: \n', reg.coef_)
print("score: ",reg.score(X_test,y_test)) 

@app.route('/')
def start():
    return "WELCOME"

@app.route("/predict", methods=["POST"])
def predict():
    print("api started")
    data = request.get_json()
    print(data,"data")
    arr = np.array(data)
    arr = arr.reshape(1,-1)
    print(arr,"arr")
    # print(loaded_model)
    predicted_data = reg.predict(arr)
    print(predicted_data[0],"predicted data")
    return json_response({"response":predicted_data[0]})

def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})


 if __name__ == '__main__':
    app.run(debug=True)