from flask import Flask,json 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def helloWorld():
    return json_response(name="sameed")

