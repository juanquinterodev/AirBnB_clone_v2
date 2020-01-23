#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models import State
start = Flask(__name__)


@start.teardown_appcontext
def close_sess(close):
    storage.close()


@start.route('/cities_by_states', strict_slashes=False)
def city_state():
    """ Display cities by states """
    objs = storage.all("State").values()
    return render_template(
                "8-cities_by_states.html",
                states=objs
            )


if __name__ == '__main__':
    start.run(host='0.0.0.0', port=5000)
