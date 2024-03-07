from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserConfirmation

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_onlu': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20, write_only=True)


class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirmation
        fields = ('code',)