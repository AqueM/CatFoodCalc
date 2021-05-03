import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

flask_app = Flask(__name__)
Bootstrap(flask_app)
flask_app.config["ENV"] = "development"
flask_app.config["TESTING"] = True
flask_app.secret_key = os.urandom(16)

from app import routes
