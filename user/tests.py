import json

from django.test import TestCase
from rest_framework.test import APIClient


class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_valid_data(self):
        response = self.client.post('/api/user/',
                                    {'email': 'new@email.com', 'password': 'new_email'},
                                    format='json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(content.get('id'))
        self.assertEqual(content.get('email'), 'new@email.com')
        self.assertTrue(content.get('created_at'))
        self.assertTrue(content.get('updated_at'))

    def test_create_user_with_invalid_data(self):
        response = self.client.post('/api/user/',
                                    {'username': 'username', 'password': 'new_user'},
                                    format='json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content.get('message'), 'Invalid data')
        self.assertFalse(content.get('id'))
        self.assertFalse(content.get('email'))
        self.assertFalse(content.get('created_at'))
        self.assertFalse(content.get('updated_at'))
