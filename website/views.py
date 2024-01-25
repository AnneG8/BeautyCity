from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def main(request):
    return render(request, 'index.html')


def service(request):
    template = loader.get_template('service.html')
    context = {}
    render_page = template.render(context, request)
    return HttpResponse(render_page)

def basehtml(request):
    template = loader.get_template('base.html')
    context = {}
    render_page = template.render(context, request)
    return HttpResponse(render_page)

