import json

from django.test import TestCase
from rest_framework.test import APIClient

URL_USER = '/api/user/'
URL_PROFILE = '/api/auth/profile/'
URL_CATEGORY = "/api/category/"
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

    def test_create_user_then_create_category_finally_get_all_category_data(self):
        response = self.client.post(URL_USER,
                                    {'email': MOCK_EMAIL, 'password': MOCK_PASSWORD},
                                    format='json')
        self.assertEqual(response.status_code, 200)

        user_id = json.loads(response.content).get('id')

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

        category_data = {
            "category_title": "Test Category",
            "category_type": "INCOME"
        }

        response_create_category = self.client.post(URL_CATEGORY, category_data)

        content = json.loads(response_create_category.content)
        self.assertEqual(content.get('message'), 'success add category')

        response_get_all_category = self.client.get(URL_CATEGORY)

        content = json.loads(response_get_all_category.content)
        self.assertTrue(content.get('category_list'))
        self.assertEqual(category_data['category_title'], content.get('category_list')[0]['category_title'])
        self.assertEqual(category_data['category_type'], content.get('category_list')[0]['category_type'])
        self.assertEqual(user_id, content.get('category_list')[0]['user'])
