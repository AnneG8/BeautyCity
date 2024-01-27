from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def base_page(request):
    return render(request, 'base.html')