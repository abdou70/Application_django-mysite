#from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("je viens tout juste de Demarrer mon stage")
