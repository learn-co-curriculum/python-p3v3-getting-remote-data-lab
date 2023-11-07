#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Sample App</h1>'

@app.route('/greet/<string:name>')
def greet(name):
    return f'<p>Welcome {name}!</p>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)