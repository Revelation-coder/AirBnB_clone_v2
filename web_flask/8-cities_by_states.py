#!/usr/bin/python3
"""
Start a Flask web application to display a list of states and their associated cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a list of states and their associated cities in an HTML page.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
