from flask import request, session
from flask_restful import Resource

from config import api
from models import User, db
from schemas import user_schema



# GET /users
class Users(Resource):

    def get(self):

        # Get logged in user only
        user = User.query.get(
            session["user_id"]
        )


        if not user:
            return {
                "error": "User not found"
            }, 404


        return user_schema.dump(user), 200



# Register users route
api.add_resource(Users,"/users")



# PATCH and DELETE /users/<id>
class UserByID(Resource):


    # PATCH /users/<id>
    def patch(self, id):

        user = User.query.get_or_404(id)


        # Only owner can update
        if user.id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403


        data = request.get_json()


        if "username" in data:
            existing = User.query.filter_by(username=data["username"]).first()

            if existing and existing.id != user.id:
                return {"errors": ["Username already exists"]}, 422
            user.username = data["username"]


        if "email" in data:
            # Check no one else already has this email
            existing = User.query.filter_by(email=data["email"]).first()
 
            if existing and existing.id != user.id:
                return {
                    "errors": ["Email already exists"]
                }, 422
            user.email = data["email"]


        if "password" in data:
            user.set_password(data["password"])


        db.session.commit()


        return user_schema.dump(user), 200



    # DELETE /users/<id>
    def delete(self, id):

        user = User.query.get_or_404(id)


        # Only owner can delete
        if user.id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403


        db.session.delete(user)
        db.session.commit()


        return {
            "message": "User deleted successfully"
        }, 200



# Register user by id route
api.add_resource(UserByID, "/users/<int:id>")