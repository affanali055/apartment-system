from django.shortcuts import render


def change_password(request):
    context = {
        'success_message': 'Password changed successfully!',
    }
    return render(request, 'todo/change_password.html', context)
