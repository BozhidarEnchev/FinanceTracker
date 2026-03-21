import datetime

from django.db import models

from FinanceTracker.common.mixins import BaseMixin


class Transaction(models.Model, BaseMixin):
    user_id = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    category_id = models.ForeignKey(
        'TransactionCategory',
        on_delete=models.CASCADE
    )
    date = models.DateField(
        default=datetime.date.today
    )
    description = models.TextField(
        blank=True,
        null=True,
    )


class TransactionCategory(models.Model, BaseMixin):
    name = models.CharField(
        max_length=100,
    )
    is_need = models.BooleanField(
        default=False,
    )
    is_saving = models.BooleanField(
        default=False,
    )


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


class FinancialAccount(models.Model, BaseMixin):
    name = models.CharField(
        max_length=100,
    )
    user_id = models.ForeignKey(
        'accounts.AppUser',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
