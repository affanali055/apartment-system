from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('apartment_register.todo_app.urls')),
    path('todo/', include('apartment_todo.todo.urls')),
]
