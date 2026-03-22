from rest_framework import serializers

from FinanceTracker.accounts.models import AppUser


class AppUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['pk', 'first_name', 'last_name', 'email']
