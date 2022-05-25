import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""

    return render(request, 'test/index.html', {
        'hostname': 'hostname',
        'count': 10
    })

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse('10')
