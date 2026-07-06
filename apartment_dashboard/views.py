from django.shortcuts import render, redirect


def dashboard(request):
    """Render the dashboard with sample todo counts."""
    context = {
        'total': 10,
        'completed': 6,
        'pending': 4,
    }
    return render(request, 'apartment_dashboard/dashboard.html', context)


def todo_list(request):
    """Simple placeholder Todo page."""
    context = {
        'todos': [
            {'title': 'Sample todo 1', 'done': True},
            {'title': 'Sample todo 2', 'done': False},
        ]
    }
    return render(request, 'apartment_dashboard/todo.html', context)


def profile(request):
    """Simple placeholder Profile page."""
    return render(request, 'apartment_dashboard/profile.html')


def logout_view(request):
    """Placeholder logout that redirects to dashboard."""
    return redirect('apartment_dashboard:dashboard')
