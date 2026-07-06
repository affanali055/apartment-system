from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/auth/', include('accounts.api_urls')),
    path('', include('apartment_register.todo_app.urls')),
    path('todo/', include('apartment_todo.todo.urls')),
    path('dashboard/', include('apartment_dashboard.urls')),
    # common typo redirect: /todo/dashbord/ -> /dashboard/
    path('todo/dashbord/', RedirectView.as_view(url='/dashboard/', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
