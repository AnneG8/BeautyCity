from random import randint
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from .backends import PhoneAuthBackend
from .models import CustomUser, Salon, Service, Employee
from .serializers import PhoneSerializer, VCodeSerializer
from .utils.smscenter import send_code


@api_view(['POST'])
def auth(request):
    serializer = PhoneSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = request.data.get('phone_number')
        user = PhoneAuthBackend.authenticate(
            request,
            username=phone_number
        )
        if not user:
            user = CustomUser.objects.create_user(phone_number=phone_number)

        # user.verification_code = randint(1000, 9999) #придумать генерацию получше
        user.verification_code = 5432
        user.is_verified = False
        user.save()
        # send_code(user.phone_number.as_e164, user.verification_code)
        return render(request, 'validate.html', {'phone_number': phone_number})
    return render(request, 'auth.html')


@api_view(['POST'])
def confirm_phone(request):
    phone_number = request.data.get('phone_number')
    serializer = VCodeSerializer(data=request.data)
    if serializer.is_valid():
        user = PhoneAuthBackend.authenticate(
            request,
            username=phone_number
        )
        if not user:
            return render(request, 'auth.html')

        if user.verification_code != serializer.get_vcode():
            context = {
                'phone_number': phone_number,
                'error_code': True
            }
            render(request, 'validate.html', context)

        user.is_verified = True
        user.save()
        login(request, user)
        redirect(f'profile/{user.id}/')
    return render(request, 'validate.html', {'phone_number': phone_number})


@login_required
def view_profile(request, user_id):
    pass


def serialize_employee(employee: Employee):
    return {
        'id': employee.id,
        'full_name': employee.__str__(),
        'photo': employee.photo.url if employee.photo else None,
        'speciality': employee.specialties.first(),
        'wexp': {
            'years': employee.work_experience.years,
            'months': employee.work_experience.months
        }
    }


def main_page(request):
    salons = Salon.objects.all()
    employees = Employee.objects.filter(specialties__isnull=False)
    services = Service.objects.all()

    context = {
        'salons': salons,
        'services': services,
        'employees': [serialize_employee(employee) for employee in employees],
    }
    return render(request, 'index.html', context)


def service(request):
    return render(request, 'service.html')


def popup_login_page(request):
    return render(request, 'popupLogin.html')

def popup_tip_page(request):
    return render(request, 'popupTip.html')

# def base_page(request):
#     return render(request, 'base.html')
