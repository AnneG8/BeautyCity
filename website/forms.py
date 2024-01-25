from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class PhoneAuthenticationForm(AuthenticationForm):
    phone_number = PhoneNumberField()


class PhoneRegistrationForm(UserCreationForm):
    phone_number = PhoneNumberField()

    class Meta(UserCreationForm.Meta):
        fields = ('phone_number',)

