#!/usr/bin/python3
"""
script starts Flask web app
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """html that shows the list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(self):
    """Close SLQAlchemy session"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port="5000", debug=True)
