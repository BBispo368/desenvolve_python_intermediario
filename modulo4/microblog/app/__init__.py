import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Config secret key
app.config['SECRET_KEY'] = "PD12345678"

# Config SQLAlchemy database URI (SQLite)
# Flask-SQLAlchemy 3.x resolves relative paths (sqlite:///microblog.db) to the instance folder.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Import routes and models to register them
from app import routes
from app.models import models
