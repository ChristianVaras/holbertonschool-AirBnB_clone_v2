#!/usr/bin/python3
"""
script starts Flask web app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def path_hbnb():
    """display text"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
