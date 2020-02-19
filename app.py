from flask import Flask,json,request 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def start():
    return "WELCOME"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    filename = "finalized_model.sav"
    loaded_model = pickle.load(open(filename,'rb'))
    predicted_data = loaded_model.predict(data)
    return json_response({response:predict_data})

def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})


 if __name__ == '__main__':
    app.run()