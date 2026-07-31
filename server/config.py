from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# Database naming conventions
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)


# Create extensions
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()
migrate = Migrate()
api = Api()


# Create Flask application
app = Flask(__name__)


# Secret key used for sessions
app.config["SECRET_KEY"] = (
    "33637955ac002d88a3a3ea47feeb059c85e35f40ca123328eb79160b16fafc1f"
)


# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitness.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)

# Initialize Flask-RESTful
api = Api(app)