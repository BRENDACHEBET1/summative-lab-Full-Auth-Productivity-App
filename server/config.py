from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api

from models import db


# Create Flask application
app = Flask(__name__)


# Secret key used to sign Flask session cookies
app.config["SECRET_KEY"] = "33637955ac002d88a3a3ea47feeb059c85e35f40ca123328eb79160b16fafc1f"


# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitness.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize database from models.py
db.init_app(app)


# Enable database migrations
migrate = Migrate(app, db)


# Initialize bcrypt for password hashing
bcrypt = Bcrypt(app)


# Initialize Flask-RESTful API
api = Api(app)