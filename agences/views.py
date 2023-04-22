from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from agence import Agence
import pandas as pd

def home(request):
     return render (request,'agences/accueil.html')

def listall(request):
     agence = Agence()
     agence.readAll()
     #return render (request,'hello')
     agence = Agence()
     agence_data = agence.data
     df = pd.DataFrame(agence_data)
     print(df)
     html = df.to_html()
     return HttpResponse("{{ html|safe }}")


