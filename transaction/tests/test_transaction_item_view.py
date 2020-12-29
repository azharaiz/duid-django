import pytz
import json
import uuid
from datetime import datetime
from collections import OrderedDict
from unittest import mock
from django.test import TestCase, Client
from transaction.models import Transaction
from category.models import Category
from authentication.models import User
from dompet.models import Dompet
from transaction.serializers import TransactionSerializer
from category.util import UtilCategory

from rest_framework.test import APIClient
from authentication.models import User

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
API_TRANSACTION_ITEM = "/api/transaction/"

class TransactionItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.basic_client = Client()
        self.mocked_date = datetime(2020, 11, 20, 20, 8, 7, 127325,
                                    tzinfo=pytz.timezone("Asia/Jakarta"))
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(
            email=OTHER_EMAIL_TEST, password=PASSWORD_TEST
            )

        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=self.mocked_date)):
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
        self.category1_object = Category.objects.get(category_title='category1')
        self.category_other_object = Category.objects.get(category_title='category_other')

        self.dompet1_object = Dompet.objects.get(account_title='dompet1')
        self.dompet_other_object = Dompet.objects.get(account_title='dompet_other')

        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=self.mocked_date)):
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

    def test_user_auth_can_delete_one_item_of_transaction(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_transaction = self.client.generic(
            method="DELETE",
            path=API_TRANSACTION_ITEM+str(self.transaction1.transaction_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(200, response_transaction.status_code)

    def test_user_not_auth_cannot_delete_one_item_of_transaction(self):
        response_transaction = self.client.generic(
            method="DELETE",
            path=API_TRANSACTION_ITEM+str(self.transaction1.transaction_id) + "/",
            content_type='application/json'
        )
        self.assertNotEqual(200, response_transaction.status_code)
        self.assertEqual(401, response_transaction.status_code)

    def test_user_auth_cannot_delete_one_item_of_transaction_when_id_wrong_or_null(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_transaction = self.client.generic(
            method="DELETE",
            path=API_TRANSACTION_ITEM+str(self.transaction1.category.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(404, response_transaction.status_code) 

    def test_user_auth_can_put_one_item_of_transaction(self):
        transaction1_id = str(self.transaction1.transaction_id)
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "dompet":self.dompet1_object.account_id,
            "category":self.category1_object.category_id,
            "amount":123.321
        }
        response_transaction = self.basic_client.put(
            API_TRANSACTION_ITEM + transaction1_id + "/",
            data, content_type="application/json"
        )
        self.assertEqual(200, response_transaction.status_code)

        transaction = Transaction.objects.get(amount=123.321)
        self.assertEqual(
            str(transaction.category.category_id),
            str(self.category1_object.category_id)
        )

    def test_user_not_auth_cannot_post_one_item_of_transaction(self):
        transaction1_id = str(self.transaction1.transaction_id)
        data = {
            "dompet":self.dompet1_object.account_id,
            "category":self.category1_object.category_id,
            "amount":123.321
        }
        response_transaction = self.basic_client.put(
            API_TRANSACTION_ITEM + transaction1_id + "/",
            data, content_type="application/json"
        )
        self.assertEqual(401, response_transaction.status_code)

    def test_user_auth_cannot_post_transaction_when_dompet_and_category_not_found(self):
        transaction1_id = str(self.transaction1.transaction_id)
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "amount":123.321
        }
        response_transaction = self.basic_client.put(
            API_TRANSACTION_ITEM + transaction1_id + "/",
            data, content_type="application/json"
        )
        self.assertEqual(200, response_transaction.status_code)
