# Project Management System

A Django-based Project Management System.

## Features Completed
- User Registration
- User Login
- User Logout
- Dashboard Access Control
- PostgreSQL Database Integration
- Environment Variable Configuration using python-decouple

## Tech Stack
- Python 3.12
- Django 6
- PostgreSQL
- Bootstrap 5
- Git & GitHub

## Setup

1. Clone repository:
git clone <repository-url>

2. Create virtual environment:
python -m venv env

3. Activate virtual environment:
env\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Create `.env` file:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=project_management_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

6. Run migrations:
python manage.py migrate

7. Start server:
python manage.py runserver
