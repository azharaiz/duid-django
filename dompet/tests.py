from datetime import datetime
from unittest import mock

import pytz
from django.test import TestCase

from dompet.models import Dompet


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
