# Personal Contact Management System

A small beginner-friendly Django project for an ICP mini project.

## Features
- Add contacts
- View all contacts
- Edit contacts
- Delete contacts after confirmation
- Store name, birthday, address, phone, and email in SQLite

## Requirements
- Python 3.10 or newer
- Internet connection for the first-time Django installation

## Setup

Open a terminal in this folder.

### 1. Create and activate a virtual environment (recommended)

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Django
```bash
python -m pip install -r requirements.txt
```

### 3. Create the database tables
```bash
python manage.py makemigrations contacts
python manage.py migrate
```

### 4. Start the website
```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Stop the server with Ctrl+C.

## Main files
- `contacts/models.py`: defines the Contact database model.
- `contacts/forms.py`: builds and validates the add/edit form.
- `contacts/views.py`: implements list, add, edit, and delete behavior.
- `contacts/urls.py`: maps app URLs to views.
- `contacts/templates/contacts/`: HTML pages.
- `contacts/static/contacts/style.css`: basic styling.
- `contact_manager/settings.py`: Django project configuration.
- `contact_manager/urls.py`: main URL routing.

This is a local classroom/demo project. It does not include user accounts or multi-user privacy controls.
