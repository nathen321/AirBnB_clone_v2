#!/usr/bin/python3
"""
A simple  minimal Flask application
"""

from flask import Flask
from markupsafe import escape
from flask import render_template
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
def nisnum(n):
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def htmlisn(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenorodd(n):
    if (n % 2) == 1:
        vod = "odd"
    else:
        vod = "even"
    return render_template(
            '6-number_odd_or_even.html', n="{:d} is {:s}".format(n, vod))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
