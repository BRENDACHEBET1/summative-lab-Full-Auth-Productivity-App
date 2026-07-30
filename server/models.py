from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from marshmallow import Schema, fields

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize the SQLAlchemy database object
db = SQLAlchemy(metadata=metadata)

#User Model
class User(db.Model):
    #Name of the table in the database
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # One user can have many exercises
    # One user can have many exercises.
    # If a user is deleted, all of their exercises are deleted too.
    exercises = db.relationship(
        "Exercise",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

#Exerxise Model
class Exercise(db.Model):
    #Name of the table
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    duration = db.Column(db.Integer)  
    calories_burned = db.Column(db.Integer)

    # Foreign key to users table
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

     # Relationship back to User
        # Allows access the owner of the exercise using exercise.user
    user = db.relationship("User", back_populates="exercises")

    def __repr__(self):
        return f"Exercise {self.name}"