from django.contrib.auth.models import BaseUserManager
from phonenumber_field.phonenumber import PhoneNumber


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password=None, username=None,
                     **extra_fields):
        if not phone_number:
            raise ValueError('Phone number is required')
        phonenumber = PhoneNumber.from_string(phone_number, 'RU')
        if not phonenumber.is_valid():
            raise ValueError(f'Invalid phone number: {phone_number}')

        if not username:
            username = phonenumber.as_e164

        user = self.model(
            username=username,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, username=None,
                    **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(phone_number, password, username, **extra_fields)
        return user

    def create_superuser(self, phone_number, password, username=None,
                         **extra_fields):
        extra_fields.setdefault("is_staff", True)
        # extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        user = self._create_user(phone_number, password, username, **extra_fields)
        return user
