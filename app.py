from flask import Flask,json,jsonify 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def helloWorld():
    return jsonify(name="sameed")

