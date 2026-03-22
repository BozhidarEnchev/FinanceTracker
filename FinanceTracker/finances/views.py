from threading import active_count

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from FinanceTracker.finances.models import Transaction, TransactionCategory, MonthlyBudget, FinancialAccount
from FinanceTracker.finances.serializers import TransactionReadSerializer, TransactionCategoryReadSerializer, \
    MonthlyBudgetReadSerializer, FinancialAccountReadSerializer, TransactionWriteSerializer, \
    TransactionCategoryWriteSerializer, MonthlyBudgetWriteSerializer, FinancialAccountWriteSerializer


class UserOwnedListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        return self.model.objects.filter(user=self.request.user)


class UserOwnedDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        return self.model.objects.filter(user=self.request.user)

class TransactionListCreateView(UserOwnedListCreateView):
    model = Transaction

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return TransactionWriteSerializer
        return TransactionReadSerializer

    def perform_create(self, serializer):
        transaction_obj = serializer.save()
        account = transaction_obj.account
        category = transaction_obj.category

        if category.is_saving:
            account.amount += transaction_obj.amount
        else:
            account.amount -= transaction_obj.amount

        account.save()


class TransactionDetailView(UserOwnedDetailView):
    model = Transaction
    serializer_class = TransactionWriteSerializer


class TransactionCategoryListCreateView(UserOwnedListCreateView):
    model = TransactionCategory

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return TransactionCategoryWriteSerializer
        return TransactionCategoryReadSerializer


class TransactionCategoryDetailView(UserOwnedDetailView):
    model = TransactionCategory
    serializer_class = TransactionCategoryWriteSerializer


class MonthlyBudgetListCreateView(UserOwnedListCreateView):
    model = MonthlyBudget

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return MonthlyBudgetWriteSerializer
        return MonthlyBudgetReadSerializer


class MonthlyBudgetDetailView(UserOwnedDetailView):
    model = MonthlyBudget
    serializer_class = MonthlyBudgetWriteSerializer


class FinancialAccountListCreateView(UserOwnedListCreateView):
    model = FinancialAccount

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return FinancialAccountWriteSerializer
        return FinancialAccountReadSerializer


class FinancialAccountDetailView(UserOwnedDetailView):
    model = FinancialAccount
    serializer_class = FinancialAccountWriteSerializer
