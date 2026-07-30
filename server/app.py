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