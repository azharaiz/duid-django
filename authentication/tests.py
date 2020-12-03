import json

from django.test import TestCase
from rest_framework.test import APIClient

from authentication.models import User

EMAIL_TEST = "test@email.com"
PASSWORD_TEST = "test12345"
TOKEN_URL = '/api/auth/token/'


class UserManagerTest(TestCase):
    def test_user_create_success(self):
        user = User.objects.create_user(email=EMAIL_TEST)
        self.assertEqual(user.email, EMAIL_TEST)
        self.assertEqual(user.__str__(), user.email)

    def test_user_create_fail(self):
        with self.assertRaises(TypeError):
            user = User.objects.create_user()
            self.assertEqual(user.email, None)

    def test_user_create_fail_null_email(self):
        with self.assertRaises(ValueError):
            user = User.objects.create_user(email=None)
            self.assertEqual(user.email, None)


class UserModelTest(TestCase):
    def test_user_save_success(self):
        user = User()
        user.email = EMAIL_TEST
        user.save()

        self.assertEqual(user.email, EMAIL_TEST)

    def test_user_save_fail(self):
        with self.assertRaises(ValueError):
            user = User()
            user.save()

            self.assertEqual(user.email, None)


class UserAuthenticationTokenTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)

    def test_user_exist_can_obtain_token(self):
        response = self.client.post(TOKEN_URL,
                                    {'email': EMAIL_TEST, 'password': PASSWORD_TEST},
                                    format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content).get('refresh'))
        self.assertTrue(json.loads(response.content).get('access'))

    def test_user_not_exist_can_not_obtain_token(self):
        response = self.client.post(TOKEN_URL,
                                    {'email': 'different@email.com', 'password': PASSWORD_TEST},
                                    format='json')
        self.assertEqual(response.status_code, 401)
        self.assertFalse(json.loads(response.content).get('refresh'))
        self.assertFalse(json.loads(response.content).get('access'))
