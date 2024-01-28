import os
from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, request

flask_app = Flask(__name__)
bootstrap = Bootstrap4(flask_app)
flask_app.config["ENV"] = "development"
flask_app.config["TESTING"] = True
flask_app.secret_key = os.urandom(16)

from app import routes
