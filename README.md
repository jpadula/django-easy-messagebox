# Django Chat Application

This is a simple chat application built using Django for the backend and JavaScript for the frontend. It allows users to send and view messages in a chatbox.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Setting up the Django Backend](#setting-up-the-django-backend)
- [Running the Application](#running-the-application)
- [Design Decisions](#design-decisions)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your system.
- Django installed (`pip install Django`).
- Basic understanding of Django, JavaScript, and APIs.

## Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/django-chat-application.git

## Project Structure

chat-application/
│
├── chatbox_project/
│   ├── chat/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

chatbox_project/: Django project directory.
chat/: Django app directory containing models, views, and URLs.
static/: Directory for static files (CSS, JavaScript).
templates/: Directory for HTML templates.
.gitignore: Git ignore file.
manage.py: Django management script.
README.md: This documentation file.

## Setting up the Django Backend

1)  python -m venv venv
	source venv/bin/activate

2) pip install -r requirements.txt

	2.1) set in .env file the DJANGO_PRODUCTION variable (false to use sqlite locally or true to use AWS). For AWS, configure in settings.py file the accesses to the database.

3) python manage.py migrate

4) python manage.py createsuperuser (step optional)

5) python manage.py runserver

## Running the Application

Access the chat application in your web browser at http://localhost:8000/.
Log in using the admin superuser credentials to access the Django admin panel at http://localhost:8000/admin/ (optional).

## Design Decisions

Backend: The backend of this chat application is built with Django, which provides a robust and secure framework for handling data storage and API endpoints. Django's ORM is used to define the database models for storing chat messages.

Frontend: The frontend is developed using HTML, CSS, and JavaScript. JavaScript is used to handle user interactions and real-time messaging. Messages are sent and received via API endpoints defined in Django views.

Database: By default, this application uses SQLite as the database for simplicity. For production use, you can configure other databases like PostgreSQL or MySQL in the Django settings.

Real-Time Messaging: Real-time messaging is not implemented in this basic version, but you can enhance it by integrating WebSockets or other real-time technologies.

Styling: Minimal styling is provided in the style.css file. You can customize the CSS to match your design preferences.