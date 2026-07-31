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

@app.before_request
def check_if_logged_in():

    open_endpoints = [
        "signup",
        "login",
        "checksession",
        "logout",
        "static"
    ]

    if request.endpoint in open_endpoints:
        return

    if "user_id" not in session:
        return {
            "error": "Unauthorized"
        }, 401

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
        user = User.query.get(session["user_id"])

        if not user:
            return {
                "error": "User not found"
            }, 404

        return user_schema.dump(user), 200


#Enpoint
api.add_resource(Users, "/users")



class UserByID(Resource):

    # PATCH /users/<id>
    def patch(self, id):

        user = User.query.get_or_404(id)

        if user.id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403

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

        if user.id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403

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


class CheckSession(Resource):

    def get(self):

        user_id = session.get("user_id")

        if not user_id:
            return {
                "error": "Not logged in"
            }, 401

        user = User.query.get(user_id)

        if not user:
            return {
                "error": "User not found"
            }, 404

        return user_schema.dump(user), 200


api.add_resource(CheckSession, "/check_session")

class Logout(Resource):

    def delete(self):

        session.pop("user_id", None)

        return {
            "message": "Logged out successfully"
        }, 200


api.add_resource(Logout, "/logout")


class Exercises(Resource):

    # GET /exercises
    def get(self):

        exercises = Exercise.query.filter_by(user_id=session["user_id"]).all()
        
        return exercises_schema.dump(exercises), 200


    # POST /exercises
    def post(self):

        data = request.get_json()

        exercise = Exercise(
            name=data["name"],
            category=data.get("category"),
            duration=data.get("duration"),
            calories_burned=data.get("calories_burned"),
            user_id=session["user_id"]
        )

        db.session.add(exercise)
        db.session.commit()

        return exercise_schema.dump(exercise), 201

api.add_resource(Exercises, "/exercises")


class ExerciseByID(Resource):

    # PATCH /exercises/<id>
    def patch(self, id):

        exercise = Exercise.query.get_or_404(id)

        if exercise.user_id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403

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
        if exercise.user_id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403

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