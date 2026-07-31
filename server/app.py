from flask import request, session

from config import app, api

from routes.auth import *
from routes.users import *
from routes.exercises import *


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


if __name__ == "__main__":
    app.run(debug=True)