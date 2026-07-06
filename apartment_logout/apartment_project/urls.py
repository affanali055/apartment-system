from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirect root to the logout page for now
    path('', RedirectView.as_view(url='/logout/', permanent=False)),
    path('', include('logout.urls')),
]
