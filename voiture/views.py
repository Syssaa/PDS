from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path


def list_voiture(request):
    return render (request,'voiture/list_voiture.html')