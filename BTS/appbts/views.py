from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views de la app 

def inicio(request):  #primer controlador(view)
    return render (request,"appbts/inicio.html")

def bts(request):
    return render (request,"appbts/bts.html")

def coreasur(request):
    return render (request,"appbts/coreasur.html")

def army(request):
    return render (request,"appbts/army.html")

def contactoFormulario(request):
    return render (request, "appbts/contactoFormulario.html")