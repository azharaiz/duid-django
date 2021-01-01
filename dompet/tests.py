import json
from datetime import datetime
from unittest import mock

import pytz
from django.test import TestCase, Client
from rest_framework.test import APIClient

from authentication.models import User
from category.util import UtilCategory as UtilDompet
from dompet.models import Dompet

ALL_DOMPET = '/api/dompet/'

EMAIL_TEST_1 = "test1@email.com"
EMAIL_TEST_2 = "test2@email.com"
PASSWORD_TEST = "test12345"
UNAUTHENTICATED_MESSAGE = "You do not have permission to perform this action."
NOT_FOUND_MESSAGE = "Not found."
UNAUTH_TITLE = 'unauth'


class DompetModelTest(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_superuser(email=EMAIL_TEST_1,
                                                    password=PASSWORD_TEST)
        self.user_2 = User.objects.create_superuser(email=EMAIL_TEST_2,
                                                    password=PASSWORD_TEST)
        self.mocked_date_1 = datetime(2020, 11, 20, 20, 8, 7, 127325,
                                      tzinfo=pytz.timezone("Asia/Jakarta"))
        self.mocked_date_2 = datetime(2020, 11, 21, 20, 8, 7, 127325,
                                      tzinfo=pytz.timezone("Asia/Jakarta"))
        self.mock_account_title_1 = "New Dompet Test 1"
        self.mock_account_title_2 = "New Dompet Test 2"

        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=self.mocked_date_1)):
            test_dompet_1 = Dompet(account_title=self.mock_account_title_1,
                                   user=self.user_1)
            test_dompet_2 = Dompet(account_title=self.mock_account_title_2,
                                   user=self.user_2)
            test_dompet_1.save()
            test_dompet_2.save()

    def test_dompet_can_be_created(self):
        all_dompet = Dompet.objects.all()

        self.assertEqual(len(all_dompet), 2)
        self.assertEqual(self.mock_account_title_1,
                         all_dompet[0].account_title)
        self.assertEqual(self.mock_account_title_2,
                         all_dompet[1].account_title)
        self.assertEqual(self.mocked_date_1, all_dompet[0].created_at)
        self.assertEqual(self.mocked_date_1, all_dompet[1].created_at)
        self.assertNotEqual(all_dompet[0].account_title,
                            all_dompet[1].account_title)
        self.assertNotEqual(all_dompet[0].account_id, all_dompet[1].account_id)

    def test_dompet_can_be_updated(self):
        dompet_1 = Dompet.objects.all()[0]
        self.assertEqual(dompet_1.created_at, self.mocked_date_1)
        self.assertEqual(dompet_1.updated_at, self.mocked_date_1)
        self.assertEqual(dompet_1.account_title, self.mock_account_title_1)
        new_title = "Updated"
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=self.mocked_date_2)):
            dompet_1.account_title = new_title
            dompet_1.save()

        self.assertEqual(dompet_1.created_at, self.mocked_date_1)
        self.assertEqual(dompet_1.updated_at, self.mocked_date_2)
        self.assertEqual(new_title, Dompet.objects.all()[0].account_title)
        # Make sure update doesnt create new object.
        self.assertEqual(len(Dompet.objects.all()), 2)

    def test_dompet_can_be_deleted(self):
        self.assertEqual(len(Dompet.objects.all()), 2)
        Dompet.objects.filter(account_title=self.mock_account_title_1).delete()
        self.assertEqual(len(Dompet.objects.all()), 1)


class DompetAPITest(TestCase):
    def setUp(self):

        self.user_1 = User.objects.create_superuser(email=EMAIL_TEST_1,
                                                    password=PASSWORD_TEST)
        self.user_2 = User.objects.create_superuser(email=EMAIL_TEST_2,
                                                    password=PASSWORD_TEST)
        self.api_client = APIClient()
        self.unauthenticated_client = Client()
        jwt_token = UtilDompet.get_jwt_token(self.api_client, EMAIL_TEST_1,
                                             PASSWORD_TEST)
        self.api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
        self.new_dompet_post = self.api_client.post(ALL_DOMPET,
                                                    {"account_title": "test 0",
                                                     "user": str(
                                                         self.user_1.id)})
        self.newly_created_dompet = json.loads(
            self.new_dompet_post.content.decode('utf-8'))

    def test_unauthenticated_should_not_be_able_to_access_any_data(self):
        response = self.unauthenticated_client.get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)

        response = self.unauthenticated_client.get(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)
        post_data = {
            'account_title': UNAUTH_TITLE,
            'user': self.user_1.id}
        response = self.unauthenticated_client.post(ALL_DOMPET,
                                                    data=post_data)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)

        response = self.unauthenticated_client.put(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/',
            data={'account_title': UNAUTH_TITLE, 'user': self.user_1.id})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)

        response = self.unauthenticated_client.delete(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_title"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)
        self.assertEqual(len(Dompet.objects.all()), 1)

    def test_user_should_not_able_to_access_other_user_dompet(self):
        api_client_user_2 = APIClient()
        jwt_token_2 = UtilDompet.get_jwt_token(api_client_user_2, EMAIL_TEST_2,
                                               PASSWORD_TEST)
        api_client_user_2.credentials(
            HTTP_AUTHORIZATION='Bearer ' + jwt_token_2)
        post_data = {
            "account_title": "test 1",
            "user": str(
                self.user_2.id)}
        user_2_new_dompet_response = api_client_user_2.post(ALL_DOMPET,
                                                            post_data)
        user_2_new_dompet_json = json.loads(
            user_2_new_dompet_response.content.decode('utf-8'))

        # user 1 access user 2
        response = self.api_client.get(
            f'{ALL_DOMPET}{user_2_new_dompet_json["account_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = self.api_client.get(f'{ALL_DOMPET}')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['count'], 1)

        response = self.api_client.put(
            f'{ALL_DOMPET}{user_2_new_dompet_json["account_id"]}/',
            data={"account_title": "changed", "user": str(self.user_2.id)})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = self.api_client.delete(
            f'{ALL_DOMPET}{user_2_new_dompet_json["account_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        # # user 2 access user 1
        response = api_client_user_2.get(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_title"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = api_client_user_2.get(f'{ALL_DOMPET}')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['count'], 1)

        response = api_client_user_2.put(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/',
            data={"account_title": "changed", "user": str(self.user_2.id)})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = api_client_user_2.delete(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        self.assertEqual(len(Dompet.objects.all()), 2)

    def test_get_all_dompet_should_return_200(self):
        response = self.api_client.get(ALL_DOMPET)
        self.assertEqual(response.status_code, 200)

    def test_dompet_count_should_be_correct(self):
        for i in range(1, 11):
            response = self.api_client.get(ALL_DOMPET)
            json_response = json.loads(response.content.decode('utf-8'))
            self.assertEqual(i, json_response['count'])
            if i <= 10:
                self.assertEqual(i, len(json_response['results']))
            self.api_client.post(ALL_DOMPET, {"account_title": f'testing {i}',
                                              "user": self.user_1.id})

    def test_pagination_should_be_correct(self):
        response = self.api_client.get(ALL_DOMPET + '?page=2')
        self.assertEqual(response.status_code, 404)

        response = self.api_client.get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNone(json_response['next'])
        self.assertIsNone(json_response['previous'])
        for i in range(25):
            self.api_client.post(ALL_DOMPET, {"account_title": f'testing {i}',
                                              "user": self.user_1.id})

        response = self.api_client.get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(json_response['next'])
        self.assertIsNone(json_response['previous'])

        response = self.api_client.get(ALL_DOMPET + '?page=2')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(json_response['next'])
        self.assertIsNotNone(json_response['previous'])

        response = self.api_client.get(ALL_DOMPET + '?page=3')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNone(json_response['next'])
        self.assertIsNotNone(json_response['previous'])

    def test_get_all_dompet_item_name_correct(self):
        for i in range(1, 10):
            self.api_client.post(ALL_DOMPET, {"account_title": f'test {i}',
                                              "user": self.user_1.id})
        response = self.api_client.get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        for i in range(len(json_response['results'])):
            self.assertEqual(json_response['results'][i]['account_title'],
                             f'test {i}')

    def test_get_one_dompet(self):
        new_dompet_response = self.api_client.get(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        json_response = json.loads(new_dompet_response.content.decode('utf-8'))
        self.assertEqual(self.newly_created_dompet, json_response)

        # Negative test, should return not found
        new_dompet_response = self.api_client.get(f'{ALL_DOMPET}randomrandom/')
        json_response = json.loads(new_dompet_response.content.decode('utf-8'))
        self.assertEqual(NOT_FOUND_MESSAGE, json_response['detail'])

    def test_create_dompet_by_posting(self):
        self.assertEqual(self.newly_created_dompet['account_title'], 'test 0')
        self.assertEqual(Dompet.objects.all()[0].account_title, 'test 0')

        # Negative test, account_title should not be empty
        response = self.api_client.post(ALL_DOMPET, {"account_title": ""})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(Dompet.objects.all()), 1)
        self.assertEqual(json_response['account_title'][0],
                         "This field may not be blank.")

    def test_delete_dompet(self):
        self.assertEqual(Dompet.objects.all()[0].account_title,
                         self.newly_created_dompet['account_title'])

        self.api_client.delete(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')

        self.assertEqual(len(Dompet.objects.all()), 0)

        response = self.api_client.delete(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        del_response_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual(NOT_FOUND_MESSAGE, del_response_json['detail'])

    def test_update_dompet(self):
        response = self.api_client.get(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response, self.newly_created_dompet)

        change_title = "changed"

        response = self.api_client.put(
            f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/',
            data={"account_title": change_title, "user": str(self.user_1.id)})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertNotEqual(json_response['account_title'],
                            self.newly_created_dompet['account_title'])
        self.newly_created_dompet['account_title'] = change_title
        self.assertEqual(json_response['account_title'],
                         self.newly_created_dompet['account_title'])
        self.assertEqual(json_response['account_id'],
                         self.newly_created_dompet['account_id'])

        # Negative test
        response = self.api_client.put(f'{ALL_DOMPET}wrong/',
                                       {"account_title": change_title,
                                        "user": str(self.user_1.id)},
                                       content_type='application/json')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)
