from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('agences.urls')),
    path('client',include('voiture.urls')),
]
