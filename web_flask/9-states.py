#!/usr/bin/python3
"""
Start a Flask web application to display a list of states and their associated cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display a list of states in an HTML page.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<string:id>', strict_slashes=False)
def states_cities(id):
    """
    Display a list of cities for a given state in an HTML page.
    """
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
