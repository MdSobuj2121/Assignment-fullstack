from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/crisis/', include('crisis.urls')),
    path('api/donations/', include('donations.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/inventory/', include('inventory.urls')),
]
