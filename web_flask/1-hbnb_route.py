#!/usr/bin/python3
from flask import Flask
start = Flask(__name__)


@start.route('/', strict_slashes=False)
def hello_world():
    """ Prints when type / """
    return 'Hello HBNB!'


@start.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints hello When someone enters / """
    return 'HBNB'


if __name__ == "__main__":
    start.run(debug=True)
