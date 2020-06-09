from django.contrib.auth import authenticate
from rest_framework.serializers import Serializer, CharField, ValidationError


class LoginSerializer(Serializer):
    username = CharField()
    password = CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError("Incorret Credentials")
