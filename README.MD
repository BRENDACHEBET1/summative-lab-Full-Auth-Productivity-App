# Fitness Tracker API

## Description

Fitness Tracker API is a Flask REST API that allows users to create accounts, log in, and manage their fitness exercises.

The application provides session-based authentication and uses Flask-Bcrypt to securely hash user passwords. Users can only access and manage their own resources through protected routes.

## Features

- User signup
- User login and logout
- Session authentication
- Password hashing with Flask-Bcrypt
- Check current user session
- Create, update, and delete exercises
- Protected routes
- User-owned exercise records

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/BRENDACHEBET1/summative-lab-Full-Auth-Productivity-App.git>
```

### 2. Navigate into the project folder

```bash
cd fitness-tracker-api
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

Using pip:

```bash
pip install -r requirements.txt
```

Or using pipenv:

```bash
pipenv install
pipenv shell
```

## Database Setup

Initialize the database migrations:

```bash
flask db init
```

Create a migration:

```bash
flask db migrate -m "Initial migration"
```

Apply migrations:

```bash
flask db upgrade
```

## Running the Application

Set the Flask application:

```bash
export FLASK_APP=app:app
```

Start the development server:

```bash
flask run
```

The API will run at:

```
http://127.0.0.1:5000
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Create a new user account |
| POST | `/login` | Log in a user |
| GET | `/check_session` | Check current logged-in user |
| DELETE | `/logout` | Log out a user |

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | Get logged-in user |
| PATCH | `/users/<id>` | Update user |
| DELETE | `/users/<id>` | Delete user |

### Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/exercises` | Get user's exercises |
| POST | `/exercises` | Create exercise |
| PATCH | `/exercises/<id>` | Update exercise |
| DELETE | `/exercises/<id>` | Delete exercise |

## Technologies Used

- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Marshmallow
- SQLite

## Database Models

### User

Fields:

- id
- username
- email
- age
- password
- created_at

### Exercise

Fields:

- id
- name
- category
- duration
- calories_burned
- user_id

## Authentication

The application uses Flask sessions to keep users logged in. Protected routes require an authenticated session.

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
Brenda Chebet.