#!/usr/bin/python3
"""This module contains a script that starts a Flask web application

    Routes:
        /: display "Hello HBNB!"
        /hbnb: display "HBNB"
        /c/<text>: display "C " followed by the value of the text variable
                    (replace underscore _ symbols with a space )

    The web application is listening on 0.0.0.0, port 5000
    """

from markupsafe import escape
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    """display some text when the root is requested"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """display a word when the route is requested"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """display C followed by the content of <text>"""
    new_text = text.replace("_", " ")
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
