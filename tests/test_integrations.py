import json

from django.test import TestCase
from rest_framework.test import APIClient

URL_USER = '/api/user/'
URL_PROFILE = '/api/auth/profile/'
MOCK_EMAIL = 'email@email.com'
MOCK_PASSWORD = 'password'


class IntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_then_check_profile(self):
        response = self.client.post(URL_USER,
                                    {'email': MOCK_EMAIL, 'password': MOCK_PASSWORD},
                                    format='json')
        self.assertEqual(response.status_code, 200)

        response_token = self.client.post(
            '/api/auth/token/',
            {
                'email': MOCK_EMAIL,
                'password': MOCK_PASSWORD
            },
            format='json'
        )

        jwt_token = json.loads(response_token.content).get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)

        response = self.client.get(URL_PROFILE, format='json')
        content = json.loads(response.content)
        self.assertEqual(MOCK_EMAIL, content.get('email'))
