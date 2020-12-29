import json
from django.test import TestCase, Client
from rest_framework.test import APIClient
from authentication.models import User
from category.models import Category
from category.util import UtilCategory

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
TOKEN_URL = '/api/auth/token/'
API_CATEGORY_ITEM = "/api/category/"

class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.basic_client = Client()
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(
            email=OTHER_EMAIL_TEST, password=PASSWORD_TEST
            )
        self.category3 = Category.objects.create(
            category_title='title3',
            user=self.user,
            category_type='INCOME'
        )
        self.category4 = Category.objects.create(
            category_title='title4',
            user=self.user,
            category_type='EXPENSE'
        )
        self.category5 = Category.objects.create(
            category_title='title5',
            user=self.other_user,
            category_type='EXPENSE'
        )
        self.not_saved_category = Category(
            category_title='not_saved',
            user=self.user,
            category_type='EXPENSE'
        )

    def test_user_auth_can_get_list_of_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(
            API_CATEGORY_ITEM, {}, format='json'
        )
        json_category_list = json.loads(response.content).get('category_list')
        self.assertEqual(200, response.status_code)

        json_category_title_list = UtilCategory.get_list_category_title(json_category_list)
        self.assertIn(self.category3.category_title, json_category_title_list)
        self.assertIn(self.category4.category_title, json_category_title_list)
        self.assertNotIn(self.not_saved_category.category_title, json_category_title_list)

    def test_user_and_other_user_has_different_data(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_user = self.client.get(
            API_CATEGORY_ITEM, {}, format='json'
        )
        self.assertEqual(200, response_user.status_code)

        token = UtilCategory.get_jwt_token(self.client, OTHER_EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_other_user = self.client.get(
            API_CATEGORY_ITEM, {}, format='json'
        )
        self.assertEqual(200, response_other_user.status_code)

        self.assertNotEqual(response_user.data, response_other_user.data)

    def test_user_is_not_authenticate_get_list_of_category(self):
        response = self.client.get(
            API_CATEGORY_ITEM, {}, format='json'
        )
        self.assertEqual(401, response.status_code)

    def test_user_auth_can_post_one_item_of_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : "tester",
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.post(API_CATEGORY_ITEM, data)
        self.assertEqual(200, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("message")
        self.assertEqual(json_category_item, "success add category")

    def test_user_not_auth_cannot_post_one_item_of_category(self):
        data = {
            "category_title" : "tester",
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.post(API_CATEGORY_ITEM, data)
        self.assertEqual(401, response_category.status_code)

    def test_user_auth_cannot_post_one_item_of_category_when_title_exist_for_that_user(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : self.category3.category_title,
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.post(API_CATEGORY_ITEM, data)
        self.assertEqual(400, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("detail")
        self.assertIn("UNIQUE constraint", json_category_item)

    def test_user_auth_cannot_post_one_item_of_category_when_type_not_income_or_expense(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : "error type",
            "category_type" : "ADD"
        }
        response_category = self.basic_client.post(API_CATEGORY_ITEM, data)
        self.assertEqual(400, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("category_type")
        self.assertIn("not a valid choice", json_category_item[0])

    def test_user_auth_can_post_one_item_of_category_when_title_exist_for_other_user(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : self.category5.category_title,
            "category_type" : self.category5.category_type
        }
        response_category = self.basic_client.post(API_CATEGORY_ITEM, data)
        self.assertEqual(200, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("message")
        self.assertEqual(json_category_item, "success add category")

    def test_user_auth_cannot_post_one_item_of_category_with__null_data(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.post(API_CATEGORY_ITEM, data)
        self.assertEqual(400, response_category.status_code)
