from rest_framework import serializers

from FinanceTracker.accounts.serializers import AppUserReadSerializer
from FinanceTracker.finances.models import Transaction, TransactionCategory, MonthlyBudget, FinancialAccount


class TransactionCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = ['pk', 'name', 'is_need', 'is_saving', 'user']

class TransactionCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = ['pk', 'name', 'is_need', 'is_saving',]

class FinancialAccountReadSerializer(serializers.ModelSerializer):
    user = AppUserReadSerializer(read_only=True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)

    class Meta:
        model = FinancialAccount
        fields = ['pk', 'name', 'user', 'amount',]


class FinancialAccountWriteSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)

    class Meta:
        model = FinancialAccount
        fields = ['pk', 'name', 'amount',]


class TransactionReadSerializer(serializers.ModelSerializer):
    user = AppUserReadSerializer(read_only=True)
    category = TransactionCategoryReadSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ['pk', 'user', 'amount', 'date', 'description', 'category', 'account',]


class TransactionWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=TransactionCategory.objects.none()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['category'].queryset = TransactionCategory.objects.filter(user=user)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)

    class Meta:
        model = Transaction
        fields = ['pk', 'amount', 'date', 'description', 'category', 'account']


class MonthlyBudgetReadSerializer(serializers.ModelSerializer):
    user = AppUserReadSerializer(read_only=True)

    class Meta:
        model = MonthlyBudget
        fields = ['pk', 'needs_budget', 'wants_budget', 'savings_target', 'month', 'year', 'user',]


class MonthlyBudgetWriteSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        return super().update(instance, validated_data)

    class Meta:
        model = MonthlyBudget
        fields = ['pk', 'needs_budget', 'wants_budget', 'savings_target', 'month', 'year',]


