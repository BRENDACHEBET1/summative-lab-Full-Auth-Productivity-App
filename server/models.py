from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from marshmallow import Schema, fields

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)

    # One user can have many exercises
    exercises = db.relationship(
        "Exercise",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    duration = db.Column(db.Integer)  
    calories_burned = db.Column(db.Integer)

    # Foreign key to users table
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

     # Relationship back to User
    user = db.relationship("User", back_populates="exercises")

    def __repr__(self):
        return f"Exercise {self.name}"