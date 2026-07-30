from marshmallow import Schema, fields
from models import *

#Converts User objetcs to JSON
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required =True)
    email = fields.Email(required=True)

   
    created_at = fields.DateTime(dump_only=True)

    #User's exercises
    exercises =  fields.Nested("ExerciseSchema", many=True)

 #Exercise Schema
 #Converts Exercise objects to JSON
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)  

    name = fields.Str(required=True)
    category = fields.Str()
    duration = fields.Int()
    calories_burned = fields.Int()

    # Foreign key linking to the user
    user_id = fields.Int(required=True)

    # Date the exercise was created
    created_at = fields.DateTime(dump_only=True)

#Schema instances

user_schema = UserSchema()
users_schema = UserSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)