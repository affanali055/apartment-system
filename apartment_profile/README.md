# Django Todo Application - Profile Page

A beginner-friendly Django Todo application with a Profile page.

## Project Structure

```
apartment_profile/
├── manage.py                          # Django management script
├── apartment_project/                 # Main project folder
│   ├── __init__.py
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Project URLs
│   ├── wsgi.py                       # WSGI configuration
├── todos/                            # Todo application
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css             # Custom CSS (no Bootstrap)
│   ├── templates/
│   │   ├── profile.html              # Profile page template
│   │   ├── dashboard.html            # Dashboard template
│   │   └── todo.html                 # Todo template
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                       # App URLs
│   └── views.py                      # Application views
└── db.sqlite3                        # SQLite database (created after migration)
```

## Features

- **Profile Page** displays:
  - Title "My Profile"
  - User Full Name
  - Username
  - Email
  - Edit Profile button

- **Navigation Bar** with links to:
  - Dashboard
  - Todo
  - Profile
  - Logout

- **Custom CSS Styling** (no Bootstrap)
- **Beginner-friendly Code** with clear comments
- **Sample Hardcoded Data** for demonstration

## Installation & Setup

### 1. Install Django

```bash
pip install django
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Accessing Pages

- **Dashboard**: `http://127.0.0.1:8000/`
- **Profile**: `http://127.0.0.1:8000/profile/`
- **Todo**: `http://127.0.0.1:8000/todo/`

## File Descriptions

### `todos/views.py`
Contains view functions that handle page rendering:
- `profile_view()` - Renders the profile page with sample user data
- `dashboard_view()` - Renders the dashboard page (placeholder)
- `todo_view()` - Renders the todo page (placeholder)

### `todos/urls.py`
URL routing configuration for the application.

### `todos/templates/profile.html`
Main profile page template with:
- Navigation bar
- User information display
- Edit Profile button

### `todos/static/css/style.css`
Custom CSS styling with:
- Responsive design
- Navigation bar styling
- Profile card layout
- Button styles
- Mobile-friendly media queries

## Sample User Data

Currently using hardcoded sample data:
```python
{
    'full_name': 'John Doe',
    'username': 'johndoe',
    'email': 'john@example.com',
}
```

To use real user data, modify `todos/views.py` to fetch from the database.

## Next Steps

To extend this application, you can:

1. **Add Edit Profile Page**: Create a form to edit user information
2. **Create User Models**: Store user data in the database
3. **Add Authentication**: Implement login/logout functionality
4. **Add Todo Models**: Create and manage todo items
5. **Add Styling**: Enhance the UI with more CSS

## Notes

- No Bootstrap framework used - pure CSS styling
- Code is beginner-friendly with clear structure
- All files are well-organized and easy to understand
- The application uses Django's built-in templating system
- Static files (CSS) are properly configured in settings.py

Enjoy your Django Todo Application!
