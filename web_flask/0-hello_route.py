#!/usr/bin/python3
"""
    Starts a Flask web application
"""

from flask import Flask


start = Flask(__name__)


@start.route('/', strict_slashes=False)
def hello_world():
    """
        Display Hello HBNB!
    """
    return ('Hello HBNB!')


if __name__ == "__main__":
    start.run()
