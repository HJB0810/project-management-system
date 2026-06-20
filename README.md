# Project Management System

A multi-user Project Management System inspired by Jira, built using Django and PostgreSQL. The application allows users to create projects, assign tasks, manage team members, track progress, and interact through a responsive dashboard.

---

## Features

### User Management

* User Registration
* Login and Logout
* Profile Management
* Password Change

### Project Management

* Create Project
* Edit Project
* Delete Project
* Add Multiple Team Members
* View Project Details

### Task Management

* Create Tasks
* Update Tasks
* Delete Tasks
* Assign Tasks to Team Members
* Set Priority and Status
* Due Date Management

### Dashboard

* Total Projects
* Total Tasks
* Completed Tasks
* Pending Tasks
* Recent Tasks
* Chart.js Visualizations

### Search and Filtering

* Search Projects
* Search Tasks
* Filter by Status and Priority

### REST APIs

Built using Django REST Framework:

#### Projects API

* GET /api/projects/
* POST /api/projects/
* PUT /api/projects/<id>/
* DELETE /api/projects/<id>/

#### Tasks API

* GET /api/tasks/
* POST /api/tasks/
* PUT /api/tasks/<id>/
* DELETE /api/tasks/<id>/

### Security

* Authentication using Django Authentication System
* Login Required Views
* Role-Based Permissions
* Task Assignment Restrictions

---

## Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL

### Frontend

* HTML
* Bootstrap 5
* Chart.js

---

## Installation

### Clone Repository

```bash
git clone https://github.com/HJB0810/project-management-system.git
cd project-management-system
```

### Create Virtual Environment

```bash
python -m venv env
```

Activate Environment

Windows:

```bash
env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Update PostgreSQL settings in `settings.py`.

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
accounts/
projects/
tasks/
dashboard/
api/
templates/
static/
core/
```

---

## Future Improvements

* Notifications
* File Attachments
* Email Alerts
* Kanban Board
* Activity Logs
* Deployment on Render

---

## Author

Harshal Bhangale



