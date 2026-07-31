
from config import db, bcrypt


#User Model
class User(db.Model):
    #Name of the table in the database
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    password = db.Column(db.String(255), nullable=True)

    # One user can have many exercises
    # One user can have many exercises.
    # If a user is deleted, all of their exercises are deleted too.
    exercises = db.relationship(
        "Exercise",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        """Hash and store a user's password."""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")


    def check_password(self, password):
        """Return True if the password matches the stored hash."""
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

#Exerxise Model
class Exercise(db.Model):
    #Name of the table
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    duration = db.Column(db.Integer)  
    calories_burned = db.Column(db.Integer)

    # Foreign key to users table
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

     # Relationship back to User
        # Allows access the owner of the exercise using exercise.user
    user = db.relationship("User", back_populates="exercises")

    def __repr__(self):
        return f"Exercise {self.name}"