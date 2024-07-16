#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from sqlalchemy.orm import scoped_session
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a list of all State objects with their cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
