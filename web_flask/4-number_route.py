#!/usr/bin/python3
"""
A simple  minimal Flask application
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def Cisfun(text):
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def bigP(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def Nisnum(n):
    if type(n) is int:
        return "{} is a numbe".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
