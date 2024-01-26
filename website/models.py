from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, AbstractUser,
                                        Group, Permission)
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from locations.models import Location
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(
        'имя пользователя',
        max_length=50
    )
    phone_number = PhoneNumberField(
        'Телефон',
        region='RU',
        unique=True
    )
    email = None

    is_verified = models.BooleanField('подтвержден', default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = [phone_number]

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        raise NotImplementedError("email_user() method is not supported in CustomUser.")


class Employee(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=70
    )
    specialties = models.ManyToManyField(
        'Speciality',
        verbose_name='сотрудники',
        related_name='employees',
    )
    # поиск по имени+фамилии

    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = 'работники'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


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
    employees = models.ManyToManyField(
        Employee,
        through='TimeSlot',
        related_name='orders',
        verbose_name='работники',
    )

    class Meta:
        verbose_name = 'салон'
        verbose_name_plural = 'салоны'

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

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(
        'название',
        max_length=40
    )

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    employee = models.ForeignKey(
        'Employee',
        verbose_name='мастер',
        related_name='time_slots',
        on_delete=models.CASCADE,
    )
    salon = models.ForeignKey(
        'Salon',
        verbose_name='салон',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    start_time = models.DateTimeField('начало')
    end_time = models.DateTimeField('конец')
    is_available = models.BooleanField(
        'в доступе',
        default=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'слот времени'
        verbose_name_plural = 'слоты времени'

    def __str__(self):
        return f'{self.start_time.strftime("%d.%m.%y %H:%M")}, {self.employee}'


class Appointment(models.Model):
    client = models.ForeignKey(
        'CustomUser',
        verbose_name='клиент',
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

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

    def __str__(self):
        return f'Запись от {self.start_time.strftime("%d.%m.%y %H:%M")}, {self.service}'


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
    open_date = models.DateTimeField(
        'дата создания',
        default=timezone.now
    )
    paid_date = models.DateTimeField(
        'дата оплаты',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'Чек №{self.id} на сумму , {self.start_time.strftime("%d.%m.%y %H:%M")}, '
