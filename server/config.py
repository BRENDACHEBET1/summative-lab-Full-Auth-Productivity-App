from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv
import os

from models import db


# Load .env variables
load_dotenv()


app = Flask(__name__)


# Secret key for Flask sessions
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitness.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize existing database object from models.py
db.init_app(app)


# Migration support
migrate = Migrate(app, db)


# Password hashing
bcrypt = Bcrypt(app)


# Flask RESTful
api = Api(app)