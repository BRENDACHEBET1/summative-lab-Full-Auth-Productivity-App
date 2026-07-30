from flask import request
from flask_restful import Resource
from config import app, api
from models import db, User, Exercise
from schemas import (
    user_schema,
    users_schema,
    exercise_schema,
    exercises_schema,
)


class Users(Resource):

    # GET /users
    def get(self):
        users = User.query.all()

        return users_schema.dump(users), 200


    # POST /users
    def post(self):

        data = request.get_json()

        user = User(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201

    #Enpoint
api.add_resource(Users, "/users")