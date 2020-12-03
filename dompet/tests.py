import json
from datetime import datetime
from unittest import mock

import pytz
from django.test import TestCase, Client

from dompet.models import Dompet

ALL_DOMPET = '/api/dompet/'


class DompetModelTest(TestCase):
    def setUp(self):
        self.mocked_date_1 = datetime(2020, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.timezone("Asia/Jakarta"))
        self.mocked_date_2 = datetime(2020, 11, 21, 20, 8, 7, 127325, tzinfo=pytz.timezone("Asia/Jakarta"))
        self.mock_account_title_1 = "New Dompet Test 1"
        self.mock_account_title_2 = "New Dompet Test 2"

        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=self.mocked_date_1)):
            test_dompet_1 = Dompet(account_title=self.mock_account_title_1)
            test_dompet_2 = Dompet(account_title=self.mock_account_title_2)
            test_dompet_1.save()
            test_dompet_2.save()

    def test_dompet_can_be_created(self):
        all_dompet = Dompet.objects.all()

        self.assertEqual(len(all_dompet), 2)
        self.assertEqual(self.mock_account_title_1, all_dompet[0].account_title)
        self.assertEqual(self.mock_account_title_2, all_dompet[1].account_title)
        self.assertEqual(self.mocked_date_1, all_dompet[0].created_at)
        self.assertEqual(self.mocked_date_1, all_dompet[1].created_at)
        self.assertNotEqual(all_dompet[0].account_title, all_dompet[1].account_title)
        self.assertNotEqual(all_dompet[0].account_id, all_dompet[1].account_id)

    def test_dompet_can_be_updated(self):
        dompet_1 = Dompet.objects.all()[0]
        self.assertEqual(dompet_1.created_at, self.mocked_date_1)
        self.assertEqual(dompet_1.updated_at, self.mocked_date_1)
        self.assertEqual(dompet_1.account_title, self.mock_account_title_1)
        new_title = "Updated"
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=self.mocked_date_2)):
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
        self.new_dompet_post = Client().post(ALL_DOMPET, {"account_title": "test 0"})
        self.newly_created_dompet = json.loads(self.new_dompet_post.content.decode('utf-8'))

    # Test endpoint
    def test_get_all_dompet_should_return_200(self):
        response = Client().get(ALL_DOMPET)
        self.assertEqual(response.status_code, 200)

    def test_dompet_count_should_be_correct(self):
        for i in range(1, 11):
            response = Client().get(ALL_DOMPET)
            json_response = json.loads(response.content.decode('utf-8'))
            self.assertEqual(i, json_response['count'])
            if i <= 10:
                self.assertEqual(i, len(json_response['results']))
            Dompet(account_title=f'testing {i}').save()

    def test_pagination_should_be_correct(self):
        response = Client().get(ALL_DOMPET + '?page=2')
        self.assertEqual(response.status_code, 404)

        response = Client().get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNone(json_response['next'])
        self.assertIsNone(json_response['previous'])
        for i in range(25):
            Dompet(account_title=f'test {i}').save()

        response = Client().get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(json_response['next'])
        self.assertIsNone(json_response['previous'])

        response = Client().get(ALL_DOMPET + '?page=2')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(json_response['next'])
        self.assertIsNotNone(json_response['previous'])

        response = Client().get(ALL_DOMPET + '?page=3')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNone(json_response['next'])
        self.assertIsNotNone(json_response['previous'])

    def test_get_all_dompet_item_name_correct(self):
        for i in range(1, 10):
            Dompet(account_title=f'test {i}').save()
        response = Client().get(ALL_DOMPET)
        json_response = json.loads(response.content.decode('utf-8'))
        for i in range(len(json_response['results'])):
            self.assertEqual(json_response['results'][i]['account_title'], f'test {i}')

    def test_get_one_dompet(self):
        new_dompet_response = Client().get(f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        json_response = json.loads(new_dompet_response.content.decode('utf-8'))
        self.assertEqual(self.newly_created_dompet, json_response)

        # Negative test, should return not found
        new_dompet_response = Client().get(f'{ALL_DOMPET}randomrandom/')
        json_response = json.loads(new_dompet_response.content.decode('utf-8'))
        self.assertEqual({"detail": "Not found."}, json_response)

    def test_create_dompet_by_posting(self):
        self.assertEqual(self.newly_created_dompet['account_title'], 'test 0')
        self.assertEqual(Dompet.objects.all()[0].account_title, 'test 0')

        # Negative test, account_title should not be empty
        response = Client().post(ALL_DOMPET, {"account_title": ""})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(Dompet.objects.all()), 1)
        self.assertEqual(json_response['account_title'][0], "This field may not be blank.")

    def test_delete_dompet(self):
        self.assertEqual(Dompet.objects.all()[0].account_title, self.newly_created_dompet['account_title'])

        Client().delete(f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')

        self.assertEqual(len(Dompet.objects.all()), 0)

        response = Client().delete(f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        del_response_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual({"detail": "Not found."}, del_response_json)

    def test_update_dompet(self):
        response = Client().get(f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response, self.newly_created_dompet)

        change_title = 'changed'

        response = Client().put(f'{ALL_DOMPET}{self.newly_created_dompet["account_id"]}/', {
            "account_id": "c6a1af05-ef26-416b-a4b1-e23b4942f50b",
            "account_title": change_title,
            "created_at": "2020-12-01T14:00:52.294269Z",
            "updated_at": "2020-12-01T17:31:04.167919Z"
        }, content_type='application/json')

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertNotEqual(json_response['account_title'], self.newly_created_dompet['account_title'])
        self.newly_created_dompet['account_title'] = change_title
        self.assertEqual(json_response['account_title'], self.newly_created_dompet['account_title'])
        self.assertEqual(json_response['account_id'], self.newly_created_dompet['account_id'])

        # Negative test
        response = Client().put(f'{ALL_DOMPET}randomm/', {
            "account_id": "c6a1af05-ef26-416b-a4b1-e23b4942f50b",
            "account_title": change_title,
            "created_at": "2020-12-01T14:00:52.294269Z",
            "updated_at": "2020-12-01T17:31:04.167919Z"
        }, content_type='application/json')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response, {"detail": "Not found."})
