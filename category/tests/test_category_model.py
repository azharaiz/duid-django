from datetime import datetime
from unittest import mock
import pytz
from django.test import TestCase
from category.models import Category
from authentication.models import User

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"

class CategoryModelTest(TestCase):
    def setUp(self):
        self.mocked_date = datetime(2020, 11, 20, 20, 8, 7, 127325,
                                    tzinfo=pytz.timezone("Asia/Jakarta"))
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(
            email=OTHER_EMAIL_TEST, password=PASSWORD_TEST
            )
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=self.mocked_date)):
            Category.objects.create(
                category_title='title1',
                user=self.user,
                category_type='INCOME'
            )
            Category.objects.create(
                category_title='title2',
                user=self.user,
                category_type='EXPENSE'
            )
            Category.objects.create(
                category_title='title3',
                user=self.other_user,
                category_type='EXPENSE'
            )
        self.category1_object = Category.objects.get(category_title='title1')
        self.category2_object = Category.objects.get(category_title='title2')
        self.category3_object = Category.objects.get(category_title='title3')

    def test_object_category_is_created(self):
        self.assertTrue(type(self.category1_object), Category)
        self.assertTrue(type(self.category2_object), Category)

    def test_category_id_auto_generated(self):
        self.assertIsNotNone(self.category1_object.category_id)
        self.assertIsNotNone(self.category2_object.category_id)

    def test_every_category_object_has_different_id(self):
        self.assertNotEqual(
            self.category1_object.category_id, self.category2_object.category_id
        )

    def test_category1_category_title_is_title1(self):
        self.assertEqual(self.category1_object.category_title, "title1")

    def test_every_category_object_has_different_title(self):
        self.assertNotEqual(
            self.category1_object.category_title, self.category2_object.category_title
        )

    def test_category1_category_type_is_income(self):
        self.assertEqual(self.category1_object.category_type, "INCOME")

    def test_every_category_object_has_different_type(self):
        self.assertNotEqual(
            self.category1_object.category_type, self.category2_object.category_type
        )

    def test_create_at_is_generated(self):
        self.assertEqual(
            self.category1_object.created_at, self.mocked_date
        )

    def test_updated_at_is_generated(self):
        self.assertEqual(
            self.category1_object.updated_at, self.mocked_date
        )

    def test_category1_category3_has_different_user(self):
        self.assertNotEqual(
            self.category1_object.user,
            self.category3_object.user
        )

    def test_category1_category2_has_same_user(self):
        self.assertEqual(
            self.category1_object.user,
            self.category2_object.user
        )
