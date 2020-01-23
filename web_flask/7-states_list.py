#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models import State
start = Flask(__name__)


@start.teardown_appcontext
def close_sess(close):
    storage.close()


@start.route('/', strict_slashes=False)
def hello_hbnb():
    """ display message when url is triggered """
    return 'Hello HBNB!'


@start.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print HBNB when in new route """
    return 'HBNB'


@start.route('/c/<text>', strict_slashes=False)
def c(text):
    """ prints C + users input """
    msg = 'C {}'.format(text)
    msg = msg.replace('_', ' ')
    return msg


@start.route('/python', strict_slashes=False)
@start.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ inputs for python and python/text routes """
    msg = 'Python {}'.format(text)
    msg = msg.replace('_', ' ')
    return msg


@start.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ print number if its an int """
    return '{} is a number'.format(n)


@start.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ html based on number given template """
    return render_template('5-number.html', number=n)


@start.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """html based on even or odd number"""
    return render_template('6-number_odd_or_even.html', number=n)


@start.route('/states_list', strict_slashes=False)
def list_states():
    """ list of states """
    states_l = storage.all("State").values()
    return render_template(
                "7-states_list.html",
                states=states_l
            )


if __name__ == '__main__':
    start.run(host='0.0.0.0', port=5000)
