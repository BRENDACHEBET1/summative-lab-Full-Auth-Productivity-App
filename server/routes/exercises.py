from flask import request, session
from flask_restful import Resource

from config import api
from models import Exercise, db
from schemas import exercise_schema, exercises_schema



# GET and POST /exercises
class Exercises(Resource):


    # GET /exercises
    def get(self):

        # Get only exercises belonging to logged in user
        exercises = Exercise.query.filter_by(
            user_id=session["user_id"]
        ).all()


        return exercises_schema.dump(exercises), 200



    # POST /exercises
    def post(self):

        data = request.get_json()


        # Create exercise for logged in user
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



# Register exercises route
api.add_resource(Exercises,"/exercises")




# PATCH and DELETE /exercises/<id>
class ExerciseByID(Resource):


    # PATCH /exercises/<id>
    def patch(self, id):

        exercise = Exercise.query.get_or_404(id)


        # Only owner can update exercise
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


        # Only owner can delete exercise
        if exercise.user_id != session["user_id"]:
            return {
                "error": "Forbidden"
            }, 403


        db.session.delete(exercise)
        db.session.commit()


        return {
            "message": "Exercise deleted successfully"
        }, 200




# Register exercise by id route
api.add_resource(ExerciseByID, "/exercises/<int:id>")