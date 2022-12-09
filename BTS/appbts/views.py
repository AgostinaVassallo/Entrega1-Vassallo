from django.shortcuts import render
from django.http import HttpResponse

# Create your views de la app 

def inicio(request):  #primer controlador(view)
    return HttpResponse("inicio")

