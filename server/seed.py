from app import app
from models import db, User, Exercise

with app.app_context():
    # Clear existing data
    Exercise.query.delete()
    User.query.delete()

    # Create users
    user1 = User(
        username="alice",
        email="alice@example.com",
        age=25
    )

    user2 = User(
        username="bob",
        email="bob@example.com",
        age=30
    )

    user3 = User(
        username="charlie",
        email="charlie@example.com",
        age=22
    )

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Create exercises
    exercise1 = Exercise(
        name="Running",
        category="Cardio",
        duration=30,
        calories_burned=300,
        user_id=user1.id
    )

    exercise2 = Exercise(
        name="Cycling",
        category="Cardio",
        duration=45,
        calories_burned=450,
        user_id=user2.id
    )

    exercise3 = Exercise(
        name="Push-ups",
        category="Strength",
        duration=15,
        calories_burned=120,
        user_id=user1.id
    )

    exercise4 = Exercise(
        name="Yoga",
        category="Flexibility",
        duration=60,
        calories_burned=180,
        user_id=user3.id
    )

    db.session.add_all([
        exercise1,
        exercise2,
        exercise3,
        exercise4
    ])

    db.session.commit()

    print("Database seeded successfully!")