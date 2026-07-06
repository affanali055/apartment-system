from django.urls import path
from . import views

urlpatterns = [
    path('', views.change_password, name='home'),
    path('change-password/', views.change_password, name='change_password'),
]
