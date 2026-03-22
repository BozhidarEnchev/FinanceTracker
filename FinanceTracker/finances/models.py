import datetime
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from FinanceTracker.common.mixins import BaseMixin

def current_year() -> int:
    return datetime.date.today().year


class Transaction(models.Model, BaseMixin):
    user = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[
            MinValueValidator(Decimal('0.01')),
        ]
    )
    category = models.ForeignKey(
        'TransactionCategory',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    account = models.ForeignKey(
        'FinancialAccount',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    date = models.DateField(
        default=datetime.date.today
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.date}-{self.amount}'

class TransactionCategory(models.Model, BaseMixin):
    name = models.CharField(
        max_length=100,
    )
    user = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='transaction_categories'
    )
    is_need = models.BooleanField(
        default=False,
    )
    is_saving = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.name}'


class MonthlyBudget(models.Model, BaseMixin):
    needs_budget = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[
            MinValueValidator(Decimal('0.00')),
        ]
    )
    wants_budget = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[
            MinValueValidator(Decimal('0.00')),
        ]
    )
    savings_target = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[
            MinValueValidator(Decimal('0.00')),
        ]
    )
    month = models.IntegerField(
        default=datetime.date.today().month,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12),
        ]
    )
    year = models.IntegerField(
        default=current_year,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(current_year),
        ]
    )
    user = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='budgets',
    )

    def __str__(self):
        return f'{self.month:02}-{self.year}'


class FinancialAccount(models.Model, BaseMixin):
    name = models.CharField(
        max_length=100,
    )
    user = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='financial_accounts',
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[
            MinValueValidator(Decimal('0.00')),
        ]
    )

    def __str__(self):
        return f'{self.name}'
