#!/usr/bin/python3
"""This module contains a script that starts a Flask web application

    The web application is listening on 0.0.0.0, port 5000
    """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """display some text when the root is requested"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
