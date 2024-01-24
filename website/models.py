from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from locations.models import Location


class Client(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=70,
        null=True,
        blank=True
    )
    phonenumber = PhoneNumberField(
        'Телефон',
        region='RU',
        unique=True
    )


class Employee(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=70,
        null=True,
        blank=True
    )
    specialties = models.ManyToManyField(
        'Speciality',
        verbose_name='сотрудники',
        related_name='employees',
    )
    salon = models.ForeignKey(
        'Salon',
        verbose_name='сотрудники',
        related_name='employees',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # поиск по имени+фамилии


class Salon(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    address = models.CharField(
        'адрес',
        max_length=100,
        blank=True,
    )
    coordinates = models.ForeignKey(
        Location,
        verbose_name='локация',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(
        'название',
        max_length=70
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    speciality = models.ForeignKey(
        'Speciality',
        verbose_name='специальность',
        related_name='services',
        on_delete=models.CASCADE,
    )


class Speciality(models.Model):
    name = models.CharField(
        'название',
        max_length=40
    )


class TimeSlot(models.Model):
    start_time = models.DateTimeField('начало')
    end_time = models.DateTimeField('конец')
    is_available = models.BooleanField(
        'в доступе',
        default=True,
        db_index=True
    )


class Appointment(models.Model):
    client = models.ForeignKey(
        'Client',
        verbose_name='клиент',
        related_name='appts',
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        'Employee',
        verbose_name='мастер',
        related_name='appts',
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        'Service',
        verbose_name='услуга',
        on_delete=models.CASCADE,
    )
    time_slot = models.OneToOneField(
        TimeSlot,
        verbose_name='слот',
        related_name='appt',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    payment = models.ForeignKey(
        'Payment',
        verbose_name='оплата',
        related_name='appts',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class Payment(models.Model):
    cost = models.DecimalField(
        'сумма',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0.00
    )
    is_paid = models.BooleanField(
        'оплачен',
        default=False
    )
    paid_date = models.DateTimeField(
        'дата оплаты',
        null=True,
        blank=True
    )
