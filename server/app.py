from flask import request, session
from flask_restful import Resource

from config import app, api
from models import User, Exercise, db
from schemas import (
    user_schema,
    users_schema,
    exercise_schema,
    exercises_schema
)
print("APP.PY LOADED")

class Signup(Resource):

    def post(self):

        data = request.get_json()

        # Check if username already exists
        existing_user = User.query.filter_by(
            username=data["username"]
        ).first()

        if existing_user:
            return {
                "error": "Username already exists"
            }, 422


        user = User(
            username=data["username"],
            email=data["email"],
            age=data.get("age")
        )

        # Hash password
        user.set_password(data["password"])

        db.session.add(user)
        db.session.commit()


        # Log user in immediately
        session["user_id"] = user.id


        return user_schema.dump(user), 201
    
# Register signup route
api.add_resource(Signup, "/signup")

class Users(Resource):

    # GET /users
    def get(self):
        users = User.query.all()

        return users_schema.dump(users), 200


    #Enpoint
api.add_resource(Users, "/users")
print("USERS ROUTE ADDED")


class UserByID(Resource):

    # PATCH /users/<id>
    def patch(self, id):

        user = User.query.get_or_404(id)

        data = request.get_json()

        if "username" in data:
            user.username = data["username"]

        if "email" in data:
            user.email = data["email"]

        db.session.commit()

        return user_schema.dump(user), 200


    # DELETE /users/<id>
    def delete(self, id):

        user = User.query.get_or_404(id)

        db.session.delete(user)
        db.session.commit()

        return {
            "message": "User deleted successfully"
        }, 200

api.add_resource(UserByID, "/users/<int:id>")

class Login(Resource):

    def post(self):

        data = request.get_json()

        user = User.query.filter_by(
            username=data["username"]
        ).first()

        if user and user.check_password(data["password"]):

            session["user_id"] = user.id

            return user_schema.dump(user), 200

        return {
            "error": "Invalid username or password"
        }, 401


api.add_resource(Login, "/login")


class Exercises(Resource):

    # GET /exercises
    def get(self):

        exercises = Exercise.query.all()

        return exercises_schema.dump(exercises), 200


    # POST /exercises
    def post(self):

        data = request.get_json()

        exercise = Exercise(
            name=data["name"],
            category=data.get("category"),
            duration=data.get("duration"),
            calories_burned=data.get("calories_burned"),
            user_id=data["user_id"]
        )

        db.session.add(exercise)
        db.session.commit()

        return exercise_schema.dump(exercise), 201

api.add_resource(Exercises, "/exercises")


class ExerciseByID(Resource):

    # PATCH /exercises/<id>
    def patch(self, id):

        exercise = Exercise.query.get_or_404(id)

        data = request.get_json()

        if "name" in data:
            exercise.name = data["name"]

        if "category" in data:
            exercise.category = data["category"]

        if "duration" in data:
            exercise.duration = data["duration"]

        if "calories_burned" in data:
            exercise.calories_burned = data["calories_burned"]

        db.session.commit()

        return exercise_schema.dump(exercise), 200


    # DELETE /exercises/<id>
    def delete(self, id):

        exercise = Exercise.query.get_or_404(id)

        db.session.delete(exercise)
        db.session.commit()

        return {
            "message": "Exercise deleted successfully"
        }, 200

api.add_resource(
    ExerciseByID,
    "/exercises/<int:id>"
)



if __name__ == "__main__":
    app.run(debug=True)