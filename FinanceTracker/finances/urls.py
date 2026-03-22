from django.urls import path
from FinanceTracker.finances.views import TransactionDetailView, TransactionListCreateView, \
    TransactionCategoryDetailView, TransactionCategoryListCreateView, MonthlyBudgetListCreateView, \
    MonthlyBudgetDetailView, FinancialAccountListCreateView, FinancialAccountDetailView

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transactions'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction'),
    path('transaction_categories/', TransactionCategoryListCreateView.as_view(), name='transaction_categories'),
    path('transaction_categories/<int:pk>/', TransactionCategoryDetailView.as_view(), name='transaction_category'),
    path('monthly_budgets/', MonthlyBudgetListCreateView.as_view(), name='monthly_budgets'),
    path('monthly_budgets/<int:pk>', MonthlyBudgetDetailView.as_view(), name='monthly_budget'),
    path('financial_accounts/', FinancialAccountListCreateView.as_view(), name='financial_accounts'),
    path('financial_accounts/<int:pk>', FinancialAccountDetailView.as_view(), name='financial_account'),
]
