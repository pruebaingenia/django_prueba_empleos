 # -*- coding : utf-8 -*-
from django.shortcuts import render

# Create your views here.
from vacantesApp import modelsV
from contactoApp.modelsC import ContactoIngenia
from . import modelsH

def renderHome(request):

    cIngenia = ContactoIngenia.objects.latest('fecha')

    data = {
            "contactoI":cIngenia,
            }

    return render(request, 'home.html', data)
