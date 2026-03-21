import datetime

from django.db import models

from FinanceTracker.common.mixins import BaseMixin


class Transaction(models.Model, BaseMixin):
    user = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    category = models.ForeignKey(
        'TransactionCategory',
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


class Target(models.Model, BaseMixin):
    needs_budget = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    wants_budget = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    savings_target = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    month = models.IntegerField()
    year = models.IntegerField()
    user = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='targets',
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
    )

    def __str__(self):
        return f'{self.name}'
