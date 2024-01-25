from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .forms import PhoneRegistrationForm


def login_client(request):
    pass

@api_view(['POST'])
def register_client(request):
    # form = PhoneRegistrationForm(request.data)

