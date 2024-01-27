from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       UserChangeForm)
from phonenumber_field.formfields import PhoneNumberField

from .models import CustomUser


class PhoneAuthForm(forms.Form):
    phone_number = PhoneNumberField()
    # agreement = forms.BooleanField(required=True, initial=False)


class PhoneRegistrationForm(UserCreationForm):
    phone_number = PhoneNumberField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('phone_number',)

class PhoneUserChangeForm(UserChangeForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = CustomUser
        fields = ('phone_number',)
