from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from FinanceTracker.accounts.models import AppUser


class AppUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['pk', 'first_name', 'last_name', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = AppUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user

    class Meta:
        model = AppUser
        fields = ["username", "email", "password"]


class LoginSerializer(TokenObtainPairSerializer):
    pass