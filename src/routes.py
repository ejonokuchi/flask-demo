"""
routes
------
Registered routes.

For more information on request handling, see:
https://flask.palletsprojects.com/en/2.0.x/api/#incoming-request-data

"""

from flask import render_template

from src import app
from src.module import bar, foo


@app.route("/")
def home() -> str:
    """
    Renders the home page.

    """
    foo()
    bar()
    context = dict()
    return render_template("home.html", **context)
