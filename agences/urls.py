from django.urls import path
from . import views

urlpatterns = [  
    path('',views.search),
    path('agences/',views.listall),
    
]
