from datetime import datetime
from unittest import mock
import pytz
from django.test import TestCase
from category.models import Category
from authentication.models import User
from dompet.models import Dompet
from transaction.models import Transaction

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"


class TransactionModelTest(TestCase):
    def setUp(self):
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
                category_title='category_other',
                user=self.other_user,
                category_type='EXPENSE'
            )
            Dompet.objects.create(
                account_title="dompet1",
                user=self.user
            )
            Dompet.objects.create(
                account_title="dompet_other",
                user=self.other_user
            )
        self.category1_object = Category.objects.get(
            category_title='category1')
        self.category_other_object = Category.objects.get(
            category_title='category_other')

        self.dompet1_object = Dompet.objects.get(account_title='dompet1')
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
                dompet=self.dompet_other_object,
                category=self.category_other_object,
                user=self.other_user,
                amount=2220.0
            )
        self.transaction1 = Transaction.objects.get(amount=100.0)
        self.transaction_other = Transaction.objects.get(amount=2220.0)

    def test_object_transaction_is_created(self):
        self.assertTrue(type(self.transaction1), Transaction)
        self.assertTrue(type(self.transaction_other), Transaction)

    def test_transaction_id_auto_generated(self):
        self.assertIsNotNone(self.transaction1.transaction_id)
        self.assertIsNotNone(self.transaction_other.transaction_id)

    def test_every_transaction_object_has_different_id(self):
        self.assertNotEqual(
            self.transaction1.transaction_id,
            self.transaction_other.transaction_id
        )

    def test_transaction1_user_is_user(self):
        self.assertEqual(self.transaction1.user, self.user)

    def test_every_transaction_object_has_different_user(self):
        self.assertNotEqual(
            self.transaction1.user, self.transaction_other.user
        )

    def test_transaction1_category_is_category1(self):
        self.assertEqual(self.transaction1.category, self.category1_object)

    def test_every_transaction_object_has_different_category(self):
        self.assertNotEqual(
            self.transaction1.category, self.transaction_other.category
        )

    def test_transaction1_dompet_is_dompet1(self):
        self.assertEqual(self.transaction1.dompet, self.dompet1_object)

    def test_every_transaction_object_has_different_dompet(self):
        self.assertNotEqual(
            self.transaction1.dompet, self.transaction_other.dompet
        )

    def test_transaction1_amount_is_100_float(self):
        self.assertEqual(self.transaction1.amount, 100.0)

    def test_every_transaction_object_has_different_amount(self):
        self.assertNotEqual(
            self.transaction1.amount, self.transaction_other.amount
        )

    def test_create_at_is_generated(self):
        self.assertEqual(
            self.transaction1.created_at, self.mocked_date
        )

    def test_updated_at_is_generated(self):
        self.assertEqual(
            self.transaction1.updated_at, self.mocked_date
        )
