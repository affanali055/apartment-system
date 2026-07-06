from django.shortcuts import render, redirect
from django.contrib.auth import logout


def logout_view(request):
    """Log the user out and show a friendly confirmation page."""
    logout(request)
    return render(request, 'logout.html')
