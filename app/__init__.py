import os
from flask import Flask, render_template, flash, request, get_flashed_messages

flask_app = Flask(__name__)
flask_app.config["ENV"] = "development"
flask_app.config["TESTING"] = True
flask_app.secret_key = os.urandom(16)

from app import routes
