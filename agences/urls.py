from django.urls import path
from . import views

urlpatterns = [  
    path('',views.home),
    path('agences/',views.listall),
]
