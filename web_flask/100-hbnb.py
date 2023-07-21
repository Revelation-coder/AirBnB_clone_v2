#!/usr/bin/python3
"""
This script starts a Flask web application and displays an HTML page similar to 8-index.html.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display the HBNB HTML page."""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    cities = sorted(storage.all("City").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    places = sorted(storage.all("Place").values(), key=lambda x: x.name)

    return render_template('100-hbnb.html',
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
