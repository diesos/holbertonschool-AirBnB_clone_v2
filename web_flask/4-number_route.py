#!/usr/bin/python3
'''script that starts a Flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    processed_text = text.replace('_', ' ')
    return f"C {processed_text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def python_route(text):
    processed_text = text.replace('_', ' ')
    return f"Python {processed_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
