# Fitness Tracker API

## Description

Fitness Tracker API is a Flask REST API that allows users to create accounts, log in, and manage their fitness exercises.

The application provides session-based authentication and uses Flask-Bcrypt to securely hash user passwords. Users can only access and manage their own resources through protected routes.

## Features

- User signup
- User login and logout
- Session-based authentication
- Password hashing with Flask-Bcrypt
- Check current user session
- Create, update, and delete exercises
- Protected API routes
- User-owned exercise records

## Project Structure

```
server/
├── app.py
├── config.py
├── models.py
├── schemas.py
├── seed.py
├── migrations/
└── routes/
    ├── auth.py
    ├── users.py
    └── exercises.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/BRENDACHEBET1/summative-lab-Full-Auth-Productivity-App.git
```

### 2. Navigate into the project folder

```bash
cd summative-lab-Full-Auth-Productivity-app
```

### 3. Navigate to the server folder

```bash
cd server
```

### 4. Create a virtual environment

```bash
python3 -m venv venv
```

### 5. Activate the virtual environment

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 6. Install dependencies


```bash
pipenv install
pipenv shell
```

## Database Setup

Apply the existing database migrations:

```bash
flask db upgrade
```

## Running the Backend

Set the Flask application:

Linux/Mac:

```bash
export FLASK_APP=app:app
```

Start the Flask server:

```bash
flask run
```

The API will run at:

```
http://127.0.0.1:5000
```

## Frontend Setup

Navigate to the frontend folder:

```bash
cd client
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm start
```

The frontend will run at:

```
http://localhost:4000
```

## API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Create a new user account |
| POST | `/login` | Log in a user |
| GET | `/check_session` | Check current logged-in user |
| DELETE | `/logout` | Log out a user |

## Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | Get logged-in user |
| PATCH | `/users/<id>` | Update user |
| DELETE | `/users/<id>` | Delete user |

## Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/exercises` | Get logged-in user's exercises |
| POST | `/exercises` | Create an exercise |
| PATCH | `/exercises/<id>` | Update an exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

## Technologies Used

- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Marshmallow
- SQLite
- React

## Database Models

### User Model

Fields:

- id
- username
- email
- age
- password
- created_at

### Exercise Model

Fields:

- id
- name
- category
- duration
- calories_burned
- user_id

## Authentication

The application uses Flask sessions to maintain user authentication.

Passwords are securely hashed using Flask-Bcrypt before being stored in the database.

Protected routes require a valid user session containing the logged-in user's ID.

Unauthorized requests return:

```json
{
    "error": "Unauthorized"
}
```

with status code:

```
401
```

## Author

Brenda Chebet