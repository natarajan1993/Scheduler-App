from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduler_app.urls')),
    path('api/', include('scheduler_api.urls')),
]
