from flask import Flask,jsonify 

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return jsonify({title:"Hello World"})

