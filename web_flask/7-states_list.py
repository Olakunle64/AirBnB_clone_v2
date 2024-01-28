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
        /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: "States"
        UL tag: with the list of all State objects present in
                DBStorage sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
    """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """close the session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def all_state():
    """list of all State objects present in
    DBStorage sorted by name (A->Z)"""
    state_list = sorted(storage.all("State").values(), key=lambda x: x.name)
    # state_list = storage.all("State")
    return render_template("7-states_list.html", state_list=state_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
