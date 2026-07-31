from flask import request, session
from flask_restful import Resource

from config import api
from models import Exercise, db
from schemas import exercise_schema, exercises_schema



# GET and POST /exercises
class Exercises(Resource):


    # GET /exercises
    def get(self):

        # Pagination params — defaults to page 1, 10 per page
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
 
        # Guard against bad/abusive values
        if page < 1:
            page = 1
        per_page = max(1, min(per_page, 100))
 
 
        # Get only exercises belonging to logged in user, paginated
        pagination = Exercise.query.filter_by(
            user_id=session["user_id"]
        ).paginate(page=page, per_page=per_page, error_out=False)
 
 
        return {
            "exercises": exercises_schema.dump(pagination.items),
            "total": pagination.total,
            "page": pagination.page,
            "per_page": pagination.per_page,
            "pages": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev
        }, 200
 


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