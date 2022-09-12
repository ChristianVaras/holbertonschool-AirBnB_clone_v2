#!/usr/bin/python3
"""
script starts Flask web app
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def path_hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def path_ctext(text):
    """display custom text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def path_python(text='is cool'):
    """display custom text
    first route statement ensures it works for:
      curl -Ls 0.0.0.0:5000/python
      curl -Ls 0.0.0.0:5000/python/
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
