from datetime import datetime
from unittest import mock
from django.test import TestCase, Client
from rest_framework.test import APIClient
import pytz

from transaction.models import Transaction
from category.models import Category
from authentication.models import User
from dompet.models import Dompet


EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
API_TRANSACTION_ITEM = "/api/transaction/"


class TransactionBaseTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.basic_client = Client()
        self.mocked_date = datetime(2020, 11, 20, 20, 8, 7, 127325,
                                    tzinfo=pytz.timezone("Asia/Jakarta"))
        self.user = User.objects.create_superuser(
            email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(
            email=OTHER_EMAIL_TEST, password=PASSWORD_TEST
        )

        with mock.patch(
            'django.utils.timezone.now',
            mock.Mock(return_value=self.mocked_date)
        ):
            Category.objects.create(
                category_title='category1',
                user=self.user,
                category_type='INCOME'
            )
            Category.objects.create(
                category_title='category2',
                user=self.user,
                category_type='INCOME'
            )
            Category.objects.create(
                category_title='category_other',
                user=self.other_user,
                category_type='EXPENSE'
            )
            Dompet.objects.create(
                account_title="dompet1",
                user=self.user
            )
            Dompet.objects.create(
                account_title="dompet2",
                user=self.user
            )
            Dompet.objects.create(
                account_title="dompet_other",
                user=self.other_user
            )
        self.category1_object = Category.objects.get(
            category_title='category1')
        self.category2_object = Category.objects.get(
            category_title='category2')
        self.category_other_object = Category.objects.get(
            category_title='category_other')

        self.dompet1_object = Dompet.objects.get(account_title='dompet1')
        self.dompet2_object = Dompet.objects.get(account_title='dompet2')
        self.dompet_other_object = Dompet.objects.get(
            account_title='dompet_other')

        with mock.patch(
            'django.utils.timezone.now',
            mock.Mock(return_value=self.mocked_date)
        ):
            Transaction.objects.create(
                dompet=self.dompet1_object,
                category=self.category1_object,
                user=self.user,
                amount=100.0
            )
            Transaction.objects.create(
                dompet=self.dompet1_object,
                category=self.category2_object,
                user=self.user,
                amount=1000.0
            )
            Transaction.objects.create(
                dompet=self.dompet2_object,
                category=self.category1_object,
                user=self.user,
                amount=300.0
            )
            Transaction.objects.create(
                dompet=self.dompet_other_object,
                category=self.category_other_object,
                user=self.other_user,
                amount=2220.0
            )
        self.transaction1 = Transaction.objects.get(amount=100.0)
        self.transaction2 = Transaction.objects.get(amount=1000.0)
        self.transaction3 = Transaction.objects.get(amount=300.0)
        self.transaction_other = Transaction.objects.get(amount=2220.0)
