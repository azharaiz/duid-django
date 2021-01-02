import json

from django.test import TestCase, Client
# Create your tests here.
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from authentication.models import User
from target.models import Target
from category.util import UtilCategory as UtilTarget

EMAIL_TEST_1 = "test1@email.com"
EMAIL_TEST_2 = "test2@email.com"
PASSWORD_TEST = "test12345"
MOCK_TARGET_TITLE_1 = "mock_target_title_1"
MOCK_TARGET_TITLE_2 = "mock_target_title_2"
MOCK_TARGET_TITLE_3 = "mock_target_title_3"
MOCK_TARGET_AMOUNT_1 = 1000
MOCK_TARGET_AMOUNT_2 = 20000
MOCK_TARGET_DATE_1 = '2020-12-30'
MOCK_TARGET_DATE_2 = '2020-12-28'
ALL_TARGET = '/api/target/'
UNAUTHENTICATED_MESSAGE = "You do not have permission to perform this action."
NOT_FOUND_MESSAGE = "Not found."
UNAUTH_TITLE = 'unauth'


class TargetModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_superuser(email=EMAIL_TEST_1,
                                                   password=PASSWORD_TEST)

        Target(target_title=MOCK_TARGET_TITLE_1,
               target_amount=MOCK_TARGET_AMOUNT_1,
               user=self.user1, due_date=MOCK_TARGET_DATE_1).save()
        Target(target_title=MOCK_TARGET_TITLE_2,
               target_amount=MOCK_TARGET_AMOUNT_2,
               user=self.user1, due_date=MOCK_TARGET_DATE_2).save()
        self.all_target = Target.objects.all()

    def test_target_can_be_created(self):
        self.assertEqual(len(self.all_target), 2)
        self.assertNotEqual(self.all_target[0], self.all_target[1])
        self.assertEqual(self.all_target[0].target_title, MOCK_TARGET_TITLE_1)
        self.assertEqual(self.all_target[1].target_title, MOCK_TARGET_TITLE_2)
        self.assertEqual(self.all_target[0].target_amount,
                         MOCK_TARGET_AMOUNT_1)
        self.assertEqual(self.all_target[1].target_amount,
                         MOCK_TARGET_AMOUNT_2)
        self.assertEqual(self.all_target[0].user, self.user1)
        self.assertEqual(self.all_target[1].user, self.user1)
        self.assertEqual(str(self.all_target[0].due_date), MOCK_TARGET_DATE_1)
        self.assertEqual(str(self.all_target[1].due_date), MOCK_TARGET_DATE_2)

    def test_target_can_be_updated(self):
        self.assertEqual(2, len(self.all_target))
        test_obj = self.all_target[0]
        self.assertNotEqual(test_obj.target_title, MOCK_TARGET_TITLE_2)
        test_obj.target_title = MOCK_TARGET_TITLE_2
        test_obj.target_amount = MOCK_TARGET_AMOUNT_2
        test_obj.due_date = MOCK_TARGET_DATE_2
        test_obj.save()
        self.assertEqual(
            Target.objects.get(target_id=test_obj.target_id).target_title,
            MOCK_TARGET_TITLE_2)
        self.assertEqual(
            Target.objects.get(target_id=test_obj.target_id).target_amount,
            MOCK_TARGET_AMOUNT_2)
        self.assertEqual(
            str(Target.objects.get(target_id=test_obj.target_id).due_date),
            MOCK_TARGET_DATE_2)
        self.assertEqual(2, len(Target.objects.all()))

    def test_target_can_be_deleted(self):
        self.assertEqual(2, len(self.all_target))
        Target.objects.all().delete()
        self.assertEqual(0, len(Target.objects.all()))

    def test_target_cant_be_less_than_0(self):
        new_test_target = Target(due_date=MOCK_TARGET_DATE_1,
                                 target_title=MOCK_TARGET_TITLE_1,
                                 target_amount=-1, user=self.user1)

        with self.assertRaises(ValidationError):
            new_test_target.save()

        self.assertEqual(2, Target.objects.all().count())

        new_test_target.target_amount = 0

        with self.assertRaises(ValidationError):
            new_test_target.save()

        self.assertEqual(2, Target.objects.all().count())

        new_test_target.target_amount = 1

        new_test_target.save()

        self.assertEqual(3, Target.objects.all().count())


class TargetApiTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_superuser(email=EMAIL_TEST_1,
                                                   password=PASSWORD_TEST)
        self.user2 = User.objects.create_superuser(email=EMAIL_TEST_2,
                                                   password=PASSWORD_TEST)
        self.api_client = APIClient()
        self.unauthenticated_client = Client()
        jwt_token = UtilTarget.get_jwt_token(self.api_client, EMAIL_TEST_1,
                                             PASSWORD_TEST)
        self.api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
        self.new_target_post = self.api_client.post(ALL_TARGET, {
            "target_title": MOCK_TARGET_TITLE_3,
            "target_amount": MOCK_TARGET_AMOUNT_1,
            "due_date": MOCK_TARGET_DATE_1,
            "user": str(self.user1.id)
        })
        self.newly_created_target = json.loads(
            self.new_target_post.content.decode('utf-8'))
        # {"target_title": "test 1", "user": str(self.user2.id),
        #  "target_amount": 200, "due_date": MOCK_TARGET_DATE_1}

    def test_unauthenticated_should_not_be_able_to_access_any_data(self):
        response = self.unauthenticated_client.get(ALL_TARGET)
        json_response = json.loads(response.content.decode('utf-8'))
        # print(json_response)
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)
        #
        response = self.unauthenticated_client.get(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)

        response = self.unauthenticated_client.post(ALL_TARGET, {
            "target_title": MOCK_TARGET_TITLE_3,
            "target_amount": MOCK_TARGET_AMOUNT_1,
            "due_date": MOCK_TARGET_DATE_1,
            "user": str(self.user1.id)
        })
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)

        response = self.unauthenticated_client.put(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/',
            data={'target_title': UNAUTH_TITLE, 'user': self.user1.id})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)

        response = self.unauthenticated_client.delete(
            f'{ALL_TARGET}{self.newly_created_target["target_title"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], UNAUTHENTICATED_MESSAGE)
        self.assertEqual(len(Target.objects.all()), 1)

    def test_user_should_not_able_to_access_other_user_target(self):
        api_client_user_2 = APIClient()
        jwt_token_2 = UtilTarget.get_jwt_token(api_client_user_2, EMAIL_TEST_2,
                                               PASSWORD_TEST)
        api_client_user_2.credentials(
            HTTP_AUTHORIZATION='Bearer ' + jwt_token_2)
        post_data = {
            "target_title": "test 1",
            "user": str(
                self.user2.id),
            "target_amount": 200,
            "due_date": MOCK_TARGET_DATE_1}
        user_2_new_target_response = api_client_user_2.post(ALL_TARGET,
                                                            post_data)
        user_2_new_target_json = json.loads(
            user_2_new_target_response.content.decode('utf-8'))

        # user 1 access user 2
        response = self.api_client.get(
            f'{ALL_TARGET}{user_2_new_target_json["target_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = self.api_client.get(f'{ALL_TARGET}')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['count'], 1)
        #
        response = self.api_client.put(
            f'{ALL_TARGET}{user_2_new_target_json["target_id"]}/',
            data={"target_title": "changed", "user": str(self.user2.id)})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = self.api_client.delete(
            f'{ALL_TARGET}{user_2_new_target_json["target_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        # # user 2 access user 1
        response = api_client_user_2.get(
            f'{ALL_TARGET}{self.newly_created_target["target_title"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = api_client_user_2.get(f'{ALL_TARGET}')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['count'], 1)

        response = api_client_user_2.put(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/',
            data={"target_title": "changed", "user": str(self.user2.id)})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        response = api_client_user_2.delete(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)

        self.assertEqual(len(Target.objects.all()), 2)

    def test_get_all_target_should_return_200(self):
        response = self.api_client.get(ALL_TARGET)
        self.assertEqual(response.status_code, 200)

    def test_target_count_should_be_correct(self):
        for i in range(1, 11):
            response = self.api_client.get(ALL_TARGET)
            json_response = json.loads(response.content.decode('utf-8'))
            self.assertEqual(i, json_response['count'])
            if i <= 10:
                self.assertEqual(i, len(json_response['results']))
            self.api_client.post(ALL_TARGET, {"target_title": "test 1",
                                              "user": str(self.user1.id),
                                              "target_amount": 200,
                                              "due_date": MOCK_TARGET_DATE_1})

    def test_pagination_should_be_correct(self):
        response = self.api_client.get(ALL_TARGET + '?page=2')
        self.assertEqual(response.status_code, 404)

        response = self.api_client.get(ALL_TARGET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNone(json_response['next'])
        self.assertIsNone(json_response['previous'])
        for _ in range(25):
            self.api_client.post(ALL_TARGET, {"target_title": "test 1",
                                              "user": str(self.user1.id),
                                              "target_amount": 200,
                                              "due_date": MOCK_TARGET_DATE_1})

        response = self.api_client.get(ALL_TARGET)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(json_response['next'])
        self.assertIsNone(json_response['previous'])

        response = self.api_client.get(ALL_TARGET + '?page=2')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNotNone(json_response['next'])
        self.assertIsNotNone(json_response['previous'])

        response = self.api_client.get(ALL_TARGET + '?page=3')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIsNone(json_response['next'])
        self.assertIsNotNone(json_response['previous'])

    def test_get_one_target(self):
        new_target_response = self.api_client.get(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/')
        json_response = json.loads(new_target_response.content.decode('utf-8'))
        self.assertEqual(self.newly_created_target, json_response)

        # Negative test, should return not found
        new_target_response = self.api_client.get(f'{ALL_TARGET}randomrandom/')
        json_response = json.loads(new_target_response.content.decode('utf-8'))
        self.assertEqual(NOT_FOUND_MESSAGE, json_response['detail'])

    def test_create_target_by_posting(self):
        self.assertEqual(self.newly_created_target['target_title'],
                         MOCK_TARGET_TITLE_3)
        self.assertEqual(Target.objects.all()[0].target_title,
                         MOCK_TARGET_TITLE_3)

        # Negative test, target_title should not be empty
        response = self.api_client.post(ALL_TARGET, {"target_title": ""})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(Target.objects.all()), 1)
        self.assertEqual(json_response['target_title'][0],
                         "This field may not be blank.")

    def test_delete_target(self):
        self.assertEqual(Target.objects.all()[0].target_title,
                         self.newly_created_target['target_title'])

        self.api_client.delete(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/')

        self.assertEqual(len(Target.objects.all()), 0)

        response = self.api_client.delete(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/')
        del_response_json = json.loads(response.content.decode('utf-8'))
        self.assertEqual(NOT_FOUND_MESSAGE, del_response_json['detail'])

    def test_update_target(self):
        response = self.api_client.get(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response, self.newly_created_target)

        change_title = "changed"

        response = self.api_client.put(
            f'{ALL_TARGET}{self.newly_created_target["target_id"]}/',
            data={"target_title": change_title, "user": str(self.user2.id),
                  "target_amount": 200, "due_date": MOCK_TARGET_DATE_1})
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertNotEqual(json_response['target_title'],
                            self.newly_created_target['target_title'])
        self.newly_created_target['target_title'] = change_title
        self.assertEqual(json_response['target_title'],
                         self.newly_created_target['target_title'])
        self.assertEqual(json_response['target_id'],
                         self.newly_created_target['target_id'])

        # Negative test
        response = self.api_client.put(f'{ALL_TARGET}wrong/',
                                       {"target_title": change_title,
                                        "user": str(self.user1.id)},
                                       content_type='application/json')
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['detail'], NOT_FOUND_MESSAGE)
