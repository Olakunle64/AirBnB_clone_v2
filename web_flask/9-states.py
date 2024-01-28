#!/usr/bin/python3
"""This module contains a script that starts a Flask web application:

    The web application is listening on 0.0.0.0, port 5000

    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and
                                    storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()

    Routes:
        /states: display a HTML page: (inside the tag BODY)
        H1 tag: "States"
        UL tag: with the list of all State objects present in
                DBStorage sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>

        /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
        H1 tag: "State: "
        H3 tag: "Cities:"
        UL tag: with the list of City objects linked to the State sorted
                by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
        H1 tag: "Not found!"

    """

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """close the session after each request"""
    storage.close()


@app.route("/states", strict_slashes=False)
def all_state():
    """list of all State objects present in
    DBStorage sorted by name (A->Z)"""
    state_list = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", state_list=state_list)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """ return the state with the id """
    key = f'State.{id}'
    if key in storage.all(State):
        state = storage.all(State)[key]
        return render_template("9-states.html", state=state)
    return "<H1>Not found!</H1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
