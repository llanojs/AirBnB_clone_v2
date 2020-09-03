#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Simple routing """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello2():
    """ Simple routing """
    return 'HBNB'


@app.route('/c/<text>')
def new_route(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """Python is cool"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
