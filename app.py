from flask import Flask,jsonify 

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "hafiz sameed"

