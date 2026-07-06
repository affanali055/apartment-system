from django.urls import path
from . import views

app_name = 'apartment_dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('todo/', views.todo_list, name='todo'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
