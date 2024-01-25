from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from website.models import Client

#User = get_user_model()

class PhoneAuthBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None

    def authenticate(self, request, phone_number=None, **kwargs):
        try:
            client = Client.objects.get(Q(phone_number=phone_number))
        except Client.DoesNotExist:
            return None

        return client
