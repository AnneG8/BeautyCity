from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def main(request):
    return render(request, 'index.html')

def manager(request):
    return render(request, 'manager-ui.html')

def notes(request):
    return render(request, 'notes.html')

def service(request):
    return render(request, 'service.html')


def serviceFinally(request):
    return render(request, 'serviceFinally.html')

def basehtml(request):
    return render (request, 'base.html')
