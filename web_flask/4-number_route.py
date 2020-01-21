#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask

start = Flask(__name__)
start.url_map.strict_slashes = False


@start.route("/")
def hello():
    """display Hello HBNB!
    """
    return "Hello HBNB!"


@start.route("/hbnb")
def hbnb():
    """display HBNB
    """
    return "HBNB"


@start.route("/c/<text>")
def c_text(text):
    """display "C " with the text of variable
    """
    return "C " + text.replace("_", " ")


@start.route("/python/")
@start.route("/python/<text>")
def python_text(text="is cool"):
    """display "Python " with the text of variable
    """
    return "Python " + text.replace("_", " ")


@start.route("/number/<int:n>")
def number(n):
    """display "n is a number" when n is an integer
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    start.run(host="0.0.0.0", port=5000)
