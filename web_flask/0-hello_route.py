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


if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000, debug=True)
