from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from phonenumber_field.phonenumber import PhoneNumber

from website.models import CustomUser, CustomUserManager

UserModel = get_user_model()

class PhoneAuthBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None:
            return
        try:
            phone_number = PhoneNumber.from_string(username, 'RU')
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return

        if (user.password is None or user.check_password(password)) \
                and self.user_can_authenticate(user):
            return user
