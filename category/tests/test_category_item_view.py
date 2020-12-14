import json

from django.test import TestCase, Client
from rest_framework.test import APIClient

from authentication.models import User
from category.models import Category
from category.util import UtilCategory


EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
API_CATEGORY_ITEM = "/api/category/"

class CategoryItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.basic_client = Client()
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(
            email=OTHER_EMAIL_TEST, password=PASSWORD_TEST
            )
        self.category6 = Category.objects.create(
            category_title='title6',
            user=self.user,
            category_type='INCOME'
        )
        self.category7 = Category.objects.create(
            category_title='title7',
            user=self.user,
            category_type='EXPENSE'
        )
        self.category8 = Category.objects.create(
            category_title='title8',
            user=self.other_user,
            category_type='EXPENSE'
        )
        self.not_saved_category = Category(
            category_title='not_saved',
            user=self.user,
            category_type='EXPENSE'
        )


    def test_user_auth_can_get_one_item_of_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category6 = self.client.generic(
            method="GET", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(200, response_category6.status_code)
        json_category_item = json.loads(response_category6.content).get("category_title")
        self.assertEqual(json_category_item, self.category6.category_title)

    def test_user_not_auth_cannot_get_one_item_of_category(self):
        response_category6 = self.client.generic(
            method="GET", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(401, response_category6.status_code)

    def test_user_auth_cannot_get_other_user_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category8 = self.client.generic(
            method="GET", path=API_CATEGORY_ITEM+str(self.category8.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(404, response_category8.status_code)

    def test_user_auth_can_delete_one_item_of_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category6 = self.client.generic(
            method="DELETE", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(200, response_category6.status_code)

    def test_user_not_auth_cannot_delete_one_item_of_category(self):
        response_category6 = self.client.generic(
            method="DELETE", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(401, response_category6.status_code)

    def test_user_auth_cannot_delete_other_user_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category8 = self.client.generic(
            method="DELETE", path=API_CATEGORY_ITEM+str(self.category8.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(404, response_category8.status_code)

    def test_user_auth_can_put_one_item_of_category(self):
        category6_id = str(self.category6.category_id)
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : "test_put",
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.put(
            API_CATEGORY_ITEM + category6_id + "/", data, content_type="application/json"
        )
        self.assertEqual(200, response_category.status_code)

        json_category_item = json.loads(response_category.content).get("message")
        self.assertEqual(json_category_item, "success add category")

        get_latest_category6 = Category.objects.get(category_id=category6_id)
        self.assertEqual(get_latest_category6.category_title, "test_put")

    def test_user_not_auth_cannot_put_one_item_of_category(self):
        category6_id = str(self.category6.category_id)
        data = {
            "category_title" : "tester",
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.put(
            API_CATEGORY_ITEM + category6_id + "/", data, content_type="application/json"
        )
        self.assertEqual(401, response_category.status_code)

        get_latest_category6 = Category.objects.get(category_id=category6_id)
        self.assertNotEqual(get_latest_category6.category_title, "tester")

    def test_user_auth_cannot_put_one_item_of_category_when_title_exist_for_that_user(self):
        category6_id = str(self.category6.category_id)
        category7_title = self.category7.category_title
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : category7_title,
            "category_type" : "INCOME"
        }
        response_category = self.basic_client.put(
            API_CATEGORY_ITEM + category6_id + "/", data, content_type="application/json"
        )
        self.assertEqual(400, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("detail")
        self.assertIn("UNIQUE constraint", json_category_item)

    def test_user_auth_cannot_put_one_item_of_category_when_type_not_income_or_expense(self):
        category6_id = str(self.category6.category_id)
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : "error type",
            "category_type" : "ADD"
        }
        response_category = self.basic_client.put(
            API_CATEGORY_ITEM + category6_id + "/", data, content_type="application/json"
        )
        self.assertEqual(400, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("category_type")
        self.assertIn("not a valid choice", json_category_item[0])

        get_latest_category6 = Category.objects.get(category_id=category6_id)
        self.assertNotEqual(get_latest_category6.category_title, "error type")

    def test_user_auth_can_put_one_item_of_category_when_title_exist_for_other_user(self):
        category6_id = str(self.category6.category_id)
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "category_title" : self.category8.category_title,
            "category_type" : self.category8.category_type
        }
        response_category = self.basic_client.put(
            API_CATEGORY_ITEM + category6_id + "/", data, content_type="application/json"
        )
        self.assertEqual(200, response_category.status_code)
        json_category_item = json.loads(response_category.content).get("message")
        self.assertEqual(json_category_item, "success add category")

        get_latest_category6 = Category.objects.get(category_id=category6_id)
        self.assertEqual(get_latest_category6.category_title, self.category8.category_title)
