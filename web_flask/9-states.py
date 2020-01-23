#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, state
start = Flask(__name__)


@start.teardown_appcontext
def close_sess(close):
    storage.close()


@start.route('/states', strict_slashes=False)
def city_state():
    """Cities by states
    """
    objs = storage.all("State").values()
    return render_template(
                "7-states_list.html",
                states=objs
            )


@start.route('/states/<id>', strict_slashes=False)
def states_int(id):
    """state is id is equal to .
    """
    objs = storage.all("State").values()
    pos = {}
    for data in objs:
        if data.id == id:
            pos = data
            break
        else:
            pos = None
    return render_template(
                "9-states.html",
                state=pos
            )


if __name__ == "__main__":
    start.run()
