from django.contrib import admin

from FinanceTracker.finances.models import Transaction, TransactionCategory, FinancialAccount, MonthlyBudget


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(MonthlyBudget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    pass

@admin.register(FinancialAccount)
class FinancialAccountAdmin(admin.ModelAdmin):
    pass
