from flask import request, session
from flask_restful import Resource

from config import api
from models import User, db
from schemas import user_schema


# POST /signup
class Signup(Resource):

    def post(self):

        data = request.get_json()

        # Check if username already exists
        existing_user = User.query.filter_by(
            username=data["username"]
        ).first()

        if existing_user:
            return {
                "errors": ["Username already exists"]
            }, 422

        #Check if eail exists
        existing_email = User.query.filter_by(email=data["email"]).first()

        if existing_email:
            return {"errors": ["Email already exists"]}, 422

        user = User(
            username=data["username"],
            email=data["email"],
            age=data.get("age")
        )

        # Hash password before saving
        user.set_password(data["password"])

        db.session.add(user)
        db.session.commit()


        # Log user in immediately
        session["user_id"] = user.id


        return user_schema.dump(user), 201


# Register signup route
api.add_resource(Signup, "/signup")



# POST /login
class Login(Resource):

    def post(self):

        data = request.get_json()

        # Find user by username
        user = User.query.filter_by(
            username=data["username"]
        ).first()


        # Check password hash
        if user and user.check_password(data["password"]):

            # Store user session
            session["user_id"] = user.id

            return user_schema.dump(user), 200


        return {
            "errors": ["Invalid username or password"]
        }, 401


# Register login route
api.add_resource(Login, "/login")

# GET /check_session
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



# Register check session route
api.add_resource(CheckSession, "/check_session")



# DELETE /logout
class Logout(Resource):

    def delete(self):

        session.pop("user_id", None)


        return {
            "message": "Logged out successfully"
        }, 200



# Register logout route
api.add_resource(Logout, "/logout")