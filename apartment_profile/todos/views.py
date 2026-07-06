from django.shortcuts import render

# Sample hardcoded user data
SAMPLE_USER = {
    'full_name': 'affan',
    'username': 'affanali',
    'email': 'affan@example.com',
}


def profile_view(request):
    """View to display the user profile page"""
    context = {
        'user_info': SAMPLE_USER,
    }
    return render(request, 'profile.html', context)


def dashboard_view(request):
    """View for the dashboard page (placeholder)"""
    return render(request, 'dashboard.html')


def todo_view(request):
    """View for the todo page (placeholder)"""
    return render(request, 'todo.html')
