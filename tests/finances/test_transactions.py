from decimal import Decimal
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from FinanceTracker.finances.models import FinancialAccount, TransactionCategory

User = get_user_model()

class TransactionTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="pass123"
        )

        self.client.force_authenticate(self.user)

        self.account = FinancialAccount.objects.create(
            name="Main",
            user=self.user,
            amount=Decimal("100.00"),
        )

        self.category_saving = TransactionCategory.objects.create(
            name="Saving",
            user=self.user,
            is_saving=True
        )

        self.category_expense = TransactionCategory.objects.create(
            name="Expense",
            user=self.user,
            is_saving=False
        )

        self.url = reverse("transactions")

    def test__create_saving_transaction_and_check_account_and_total_amount(self):
        data = {
            "amount": "50.00",
            "category": self.category_saving.id,
            "account": self.account.id,
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)

        self.account.refresh_from_db()
        self.user.refresh_from_db()

        self.assertEqual(self.account.amount, Decimal("150.00"))

    def test__create_expense_transaction_and_check_account_and_total_amount(self):
        data = {
            "amount": "50.00",
            "category": self.category_expense.id,
            "account": self.account.id,
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)

        self.account.refresh_from_db()
        self.user.refresh_from_db()

        self.assertEqual(self.account.amount, Decimal("50.00"))