from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    x = 1 + 1
    return 'Hello, World!'


app.run(host='0.0.0.0', port =5000)