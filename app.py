from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!!!!!!!"

@app.route('/square/<int:num>')
def square(num):
    return str(num**2)



