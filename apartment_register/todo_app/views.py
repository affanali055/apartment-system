from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('/todo/')
    else:
        form = AuthenticationForm()

    return render(request, 'todo_app/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if not full_name or not username or not email or not password1 or not password2:
            messages.error(request, 'Please fill in all fields.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username is already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = full_name
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

    return render(request, 'todo_app/register.html')
