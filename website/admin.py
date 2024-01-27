from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import PhoneRegistrationForm, PhoneUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = PhoneRegistrationForm
    form = PhoneUserChangeForm
    model = CustomUser
    list_display = ('username', 'phone_number', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'phone_number')}),
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
