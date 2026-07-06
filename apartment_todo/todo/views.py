from django.shortcuts import render


def todo_page(request):
    todos = [
        'Buy groceries',
        'Pay electricity bill',
        'Clean the kitchen',
    ]
    return render(request, 'todo/todo.html', {'todos': todos})
