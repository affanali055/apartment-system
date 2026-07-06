# Quick Start Guide

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Step-by-Step Setup

### 1. Install Django
```bash
pip install django
```

### 2. Navigate to Project Directory
```bash
cd apartment_profile
```

### 3. Run Migrations
This sets up the database:
```bash
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
```

### 5. View the Application
Open your browser and go to:
- Profile Page: `http://127.0.0.1:8000/profile/`
- Dashboard: `http://127.0.0.1:8000/`
- Todo: `http://127.0.0.1:8000/todo/`

## Project Overview

This is a beginner-friendly Django project with:

✅ **HTML Templates**: Located in `todos/templates/`
✅ **CSS Styling**: Located in `todos/static/css/style.css`
✅ **Django Views**: Defined in `todos/views.py`
✅ **URL Routing**: Configured in `todos/urls.py`
✅ **Navigation Bar**: Available on all pages
✅ **Sample Data**: Hardcoded user information
✅ **Responsive Design**: Mobile-friendly layout

## File Locations

| File | Purpose |
|------|---------|
| `todos/views.py` | View functions for rendering pages |
| `todos/urls.py` | URL routing configuration |
| `todos/templates/profile.html` | Profile page HTML |
| `todos/static/css/style.css` | All CSS styling |
| `apartment_project/settings.py` | Django settings |
| `apartment_project/urls.py` | Project-level URL config |

## Editing the Profile Page

### To change user information:
Edit `todos/views.py` and modify the `SAMPLE_USER` dictionary:
```python
SAMPLE_USER = {
    'full_name': 'Your Name',
    'username': 'your_username',
    'email': 'your@email.com',
}
```

### To change styling:
Edit `todos/static/css/style.css` directly

### To change HTML layout:
Edit `todos/templates/profile.html`

## Stopping the Server
Press `Ctrl+C` in your terminal

## Need Help?
- Django Documentation: https://docs.djangoproject.com/
- Project README: See README.md file

Happy coding!
