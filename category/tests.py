import pytz
import json
import uuid
from .util import UtilCategory
from datetime import datetime
from collections import OrderedDict
from unittest import mock
from django.test import TestCase, Client
from .models import Category
from .serializers import CategorySerializer

from rest_framework.test import APIClient
from authentication.models import User

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
TOKEN_URL = '/api/auth/token/'
API_CATEGORY_ITEM = "/api/category/"

class CategoryModelTest(TestCase):
    def setUp(self):
        self.mocked_date = datetime(2020, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.timezone("Asia/Jakarta"))
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(email=OTHER_EMAIL_TEST, password=PASSWORD_TEST)
        category1 = ""
        category2 = ""
        category3 = ""
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=self.mocked_date)):
            category1 = Category.objects.create(
                category_title = 'title1',
                user = self.user,
                category_type = 'INCOME'
            )
            category2 = Category.objects.create(
                category_title = 'title2',
                user = self.user,
                category_type = 'EXPENSE'
            )
            category3 = Category.objects.create(
                category_title = 'title3',
                user = self.other_user,
                category_type = 'EXPENSE'
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

    def test_category1_category_type_is_INCOME(self):
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

class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.basic_client = Client()
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(email=OTHER_EMAIL_TEST, password=PASSWORD_TEST)
        self.category3 = Category.objects.create(
                category_title = 'title3',
                user = self.user,
                category_type = 'INCOME'
        )
        self.category4 = Category.objects.create(
            category_title = 'title4',
            user = self.user,
            category_type = 'EXPENSE'
        )
        self.category5 = Category.objects.create(
            category_title = 'title5',
            user = self.other_user,
            category_type = 'EXPENSE'
        )
        self.not_saved_category = Category(
            category_title = 'not_saved',
            user = self.user,
            category_type = 'EXPENSE'
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

    def test_user_auth_cannot_post_one_item_of_category_when_type_not_INCOME_or_EXPENSE(self):
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

class CategoryItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.basic_client = Client()
        self.user = User.objects.create_superuser(email=EMAIL_TEST, password=PASSWORD_TEST)
        self.other_user = User.objects.create_superuser(email=OTHER_EMAIL_TEST, password=PASSWORD_TEST)
        self.category6 = Category.objects.create(
                category_title = 'title6',
                user = self.user,
                category_type = 'INCOME'
        )
        self.category7 = Category.objects.create(
            category_title = 'title7',
            user = self.user,
            category_type = 'EXPENSE'
        )
        self.category8 = Category.objects.create(
            category_title = 'title8',
            user = self.other_user,
            category_type = 'EXPENSE'
        )
        self.not_saved_category = Category(
            category_title = 'not_saved',
            user = self.user,
            category_type = 'EXPENSE'
        )


    def test_user_auth_can_get_one_item_of_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category6 = self.client.generic(
            method="GET", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/", content_type='application/json'
        )
        self.assertEqual(200, response_category6.status_code)
        json_category_item = json.loads(response_category6.content).get("category_title")
        self.assertEqual(json_category_item, self.category6.category_title)

    def test_user_not_auth_cannot_get_one_item_of_category(self):
        response_category6 = self.client.generic(
            method="GET", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/", content_type='application/json'
        )
        self.assertEqual(401, response_category6.status_code)
    
    def test_user_auth_cannot_get_other_user_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category8 = self.client.generic(
            method="GET", path=API_CATEGORY_ITEM+str(self.category8.category_id) + "/", content_type='application/json'
        )
        self.assertEqual(404, response_category8.status_code)
    
    def test_user_auth_can_delete_one_item_of_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category6 = self.client.generic(
            method="DELETE", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/", content_type='application/json'
        )
        self.assertEqual(200, response_category6.status_code)
    
    def test_user_not_auth_cannot_delete_one_item_of_category(self):
        response_category6 = self.client.generic(
            method="DELETE", path=API_CATEGORY_ITEM+str(self.category6.category_id) + "/", content_type='application/json'
        )
        self.assertEqual(401, response_category6.status_code)

    def test_user_auth_cannot_delete_other_user_category(self):
        token = UtilCategory.get_jwt_token(self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_category8 = self.client.generic(
            method="DELETE", path=API_CATEGORY_ITEM+str(self.category8.category_id) + "/", content_type='application/json'
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

        get_latest_category6 = Category.objects.get(category_id = category6_id)
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

    def test_user_auth_cannot_put_one_item_of_category_when_type_not_INCOME_or_EXPENSE(self):
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
