from django.urls import path

from .views import UserDetailAPIView, UserRegistrationAPIView, UserValidationAPIView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('me/', UserDetailAPIView.as_view(), name='api-user-detail'),
    path('validate/', UserValidationAPIView.as_view(), name='api-validate'),
]
