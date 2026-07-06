from django.urls import path
from .views import todo_page

urlpatterns = [
    path('', todo_page, name='todo_page'),
]
