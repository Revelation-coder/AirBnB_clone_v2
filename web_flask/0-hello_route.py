#!/usr/bin/python3
"""
0-hello_route.py - Start a Flask web application

This script starts a Flask web application that listens on 0.0.0.0, port 5000.

Routes:
    /: display "Hello HBNB!"
    (You must use the option strict_slashes=False in your route definition)
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
