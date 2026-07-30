from sqlalchemy import schema, fields
from models import *

#Converts User objetcs to JSON
class UserSchema(schema):
    id = fields.Int
    username = fields.Str(required =True)
    email = fields.Email(required=True)

    password = fields.Str(load_only=True)
    created_at = fields.DateTime(dump_only=True)

    #User's exercises
    exercises =  fields.Nested("ExerciseSchema", many=True)

    