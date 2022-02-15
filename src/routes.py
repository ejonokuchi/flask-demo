"""
routes
------
Registered routes.

For more information on request handling, see:
https://flask.palletsprojects.com/en/2.0.x/api/#incoming-request-data

"""

from flask import jsonify, request

from src import app
from src.module import bar, foo


@app.route("/", methods=["GET"])
def get() -> str:
    """
    Handles a GET request to `/`.

    """
    foo()
    return "Success!"


@app.route("/submit", methods=["POST"])
def post():
    """
    Handles a POST request to `/submit`.

    """
    bar()
    data = request.get_json()
    return data if data is not None else jsonify(dict())
