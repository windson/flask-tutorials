from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    msg = 'Hello, world!'
    return msg


app.run(host='0.0.0.0', port =5000)