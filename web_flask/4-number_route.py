#!/usr/bin/python3
"""This module contains a script that starts a Flask web application

    Routes:
        /: display "Hello HBNB!"
        /hbnb: display "HBNB"
        /c/<text>: display "C " followed by the value of the text variable
                    (replace underscore _ symbols with a space )
        /python/<text>: display "Python ", followed by the value of the
                        text variable (replace underscore _ symbols with
                        a space )
        /number/<n>: display "n is a number" only if n is an integer

    The web application is listening on 0.0.0.0, port 5000
    """


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
    new_text = str(text).replace("_", " ")
    return f'C {new_text}'


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """display Python followed by the content of <text>"""
    new_text = str(text).replace("_", " ")
    return f'Python {new_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display a number only if it's an integer"""
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
