from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, UserRegistrationView,
    UserRegistrationAPIView, UserDetailAPIView, UserValidationAPIView
)

app_name = 'accounts'

urlpatterns = [
    # Template-based views
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    # API endpoints
    path('api/register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('api/me/', UserDetailAPIView.as_view(), name='api-user-detail'),
    path('api/validate/', UserValidationAPIView.as_view(), name='api-validate'),
]
