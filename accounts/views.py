from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from .serializers import UserRegistrationForm, UserRegistrationSerializer, UserDetailSerializer


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


class UserRegistrationView(CreateView):
    """
    User registration view using CreateView.
    """
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Account created successfully! You can now log in.'
        )
        return response
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{field}: {error}')
        return super().form_invalid(form)


# ===================== REST API Views =====================

class UserRegistrationAPIView(APIView):
    """
    API view for user registration.
    
    POST /api/auth/register/
    {
        "username": "john_doe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "securepassword123",
        "password_confirm": "securepassword123"
    }
    """
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        """
        Register a new user with email, username, and password validation.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'status': 'success',
                    'message': 'User registered successfully!',
                    'data': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    }
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                'status': 'error',
                'message': 'Registration failed. Please check your input.',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UserDetailAPIView(APIView):
    """
    API view to retrieve authenticated user details.
    
    GET /api/auth/me/
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        """
        Get the authenticated user's details.
        """
        serializer = UserDetailSerializer(request.user)
        return Response(
            {
                'status': 'success',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


class UserValidationAPIView(APIView):
    """
    API view for validating username and email availability.
    
    POST /api/auth/validate/
    {
        "username": "john_doe",
        "email": "john@example.com"
    }
    """
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        """
        Validate username and email availability.
        """
        errors = {}
        
        username = request.data.get('username')
        email = request.data.get('email')
        
        if username:
            if User.objects.filter(username=username).exists():
                errors['username'] = 'This username is already taken.'
        
        if email:
            if User.objects.filter(email=email).exists():
                errors['email'] = 'This email address is already registered.'
        
        if errors:
            return Response(
                {
                    'status': 'error',
                    'message': 'Validation failed',
                    'errors': errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            {
                'status': 'success',
                'message': 'Username and email are available.'
            },
            status=status.HTTP_200_OK
        )
