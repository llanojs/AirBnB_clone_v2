#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

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
def c_route(text):
    """ Routing with a string as dynamic parameter """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ Routing with a string as dynamic parameter """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def isanumber(n):
    """ Routing with a int as dynamic parameter """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Routing with a template as dynamic parameter """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Routing with a template as dynamic parameter """
    parity = ""
    if n % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
