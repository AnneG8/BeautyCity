from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

User = get_user_model()


class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        validators=PhoneNumberField().validators
    )


class VCodeSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()
    num3 = serializers.IntegerField()
    num4 = serializers.IntegerField()

    def get_vcode(self):
        return int(f'{self.num1}{self.num2}{self.num3}{self.num4}')

