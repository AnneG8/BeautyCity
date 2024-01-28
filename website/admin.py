from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import PhoneRegistrationForm, PhoneUserChangeForm
from .models import (CustomUser, Employee, Salon, Service, Speciality,
                     TimeSlot, Appointment, Payment, Employee_Speciality)


class EmployeeSpecialityInline(admin.TabularInline):
    model = Employee_Speciality
    extra = 1


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


class TimeSlotInline(admin.TabularInline):
    model = TimeSlot
    extra = 1


class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = PhoneRegistrationForm
    form = PhoneUserChangeForm
    model = CustomUser
    inlines = [
        AppointmentInline
    ]
    list_display = ('username', 'phone_number', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'photo', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_superuser',),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        EmployeeSpecialityInline,
        TimeSlotInline
    ]


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    inlines = [
        TimeSlotInline
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    inlines = [
        ServiceInline
    ]


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
