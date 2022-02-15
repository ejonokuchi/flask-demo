"""
init
----
Creates the application object and register the routes.

"""

from flask import Flask

app = Flask(__name__)

# Routes
from src import routes
