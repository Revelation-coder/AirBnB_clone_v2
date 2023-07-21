#!/usr/bin/python3
"""
5-number_template.py - Start a Flask web application

This script starts a Flask web application that listens on 0.0.0.0, port 5000.

Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C ", followed by the value of the text variable
              (replace underscore _ symbols with a space)
    /python/(<text>): display "Python ", followed by the value of the text variable
                      (replace underscore _ symbols with a space)
                      The default value of text is "is cool"
    /number/<n>: display "{} is a number" only if n is an integer
    /number_template/<n>: display an HTML page with the message "Number: n" inside the H1 tag, only if n is an integer
    (You must use the option strict_slashes=False in your route definition)
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
