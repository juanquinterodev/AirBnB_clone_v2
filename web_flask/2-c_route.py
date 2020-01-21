#!/usr/bin/python3
from flask import Flask
start = Flask(__name__)


@start.route('/', strict_slashes=False)
def hello_world():
    """ Prints when enters / """
    return 'Hello HBNB!'


@start.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints when someone enters /hbnb """
    return 'HBNB'


@start.route('/c/<text>', strict_slashes=False)
def c_text(text=None):
    """ Prints when someone enters /c/<text> """
    if text is not None:
        return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    start.run(debug=True)
