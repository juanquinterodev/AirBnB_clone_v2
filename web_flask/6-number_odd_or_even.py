#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template

start = Flask(__name__)
start.url_map.strict_slashes = False


@start.route("/")
def hello():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@start.route("/hbnb")
def hbnb():
    """display HBNB"""
    return "HBNB"


@start.route("/c/<text>")
def c_text(text):
    """display "C " wih the text of variable
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
    """display "n is a number" if n is an integer
    """
    return "{} is a number".format(n)


@start.route("/number_template/<int:n>")
def number_template(n):
    """display a HTML page if n is an integer
    """
    return render_template("5-number.html", n=n)


@start.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """display a HTML page if n is an integer
    """
    if (n % 2 == 0):
        text = "even"
        return render_template("6-number_odd_or_even.html", n=n, text=text)
    else:
        text = "odd"
        return render_template("6-number_odd_or_even.html", n=n, text=text)


if __name__ == "__main__":
    start.run(host="0.0.0.0", port=5000)
