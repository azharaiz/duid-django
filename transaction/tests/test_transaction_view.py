import json

from transaction.models import Transaction
from category.util import UtilCategory
from .test_base_transaction import TransactionBaseTest

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
API_TRANSACTION_ITEM = "/api/transaction/"


class TransactionViewTest(TransactionBaseTest):

    def test_user_is_not_authenticate_get_list_of_transaction(self):
        response = self.client.get(
            API_TRANSACTION_ITEM, {}, format='json'
        )
        self.assertEqual(401, response.status_code)

    def test_user_auth_can_get_list_of_transaction_by_category(self):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        id_category1 = str(self.category1_object.category_id)
        id_category2 = str(self.category2_object.category_id)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(
            API_TRANSACTION_ITEM + "?category_id=" + id_category1,
            {}, format='json'
        )

        json_transaction_list = json.loads(
            response.content).get('transaction_list')
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(json_transaction_list))
        self.assertIn(
            id_category1,
            json_transaction_list[0].get("category"))
        self.assertNotIn(
            id_category2,
            json_transaction_list[1].get("category"))

    def test_user_auth_can_get_list_of_transaction_by_dompet(self):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        id_dompet1 = str(self.dompet1_object.account_id)
        id_dompet2 = str(self.dompet2_object.account_id)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(
            API_TRANSACTION_ITEM + "?account_id=" + id_dompet1,
            {}, format='json'
        )

        json_transaction_list = json.loads(
            response.content).get('transaction_list')
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(json_transaction_list))
        self.assertIn(
            id_dompet1,
            json_transaction_list[0].get("dompet"))
        self.assertNotIn(
            id_dompet2,
            json_transaction_list[1].get("dompet"))

    def test_user_auth_can_get_list_of_transaction_by_dompet_and_category(
        self
    ):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        id_dompet1 = str(self.dompet1_object.account_id)
        id_dompet2 = str(self.dompet2_object.account_id)
        id_category1 = str(self.category1_object.category_id)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(
            API_TRANSACTION_ITEM + "?account_id=" +
            id_dompet1 + "&category_id=" + id_category1,
            {}, format='json'
        )

        json_transaction_list = json.loads(
            response.content).get('transaction_list')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(json_transaction_list))
        self.assertIn(
            id_dompet1,
            json_transaction_list[0].get("dompet"))
        self.assertNotIn(
            id_dompet2,
            json_transaction_list[0].get("dompet"))

    def test_user_auth_can_get_list_of_transaction_whitout_filter(self):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        id_dompet1 = str(self.dompet1_object.account_id)
        id_dompet2 = str(self.dompet2_object.account_id)
        id_category1 = str(self.category1_object.category_id)
        id_category2 = str(self.category2_object.category_id)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(
            API_TRANSACTION_ITEM,
            {}, format='json'
        )

        json_transaction_list = json.loads(
            response.content).get('transaction_list')
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(json_transaction_list))
        self.assertIn(
            id_dompet1,
            json_transaction_list[0].get("dompet"))
        self.assertIn(
            id_category1,
            json_transaction_list[0].get("category"))
        self.assertIn(
            id_dompet1,
            json_transaction_list[1].get("dompet"))
        self.assertIn(
            id_category2,
            json_transaction_list[1].get("category"))
        self.assertIn(
            id_dompet2,
            json_transaction_list[2].get("dompet"))

    def test_user_auth_can_post_one_item_of_transaction(self):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "dompet": self.dompet1_object.account_id,
            "category": self.category1_object.category_id,
            "amount": 123.321
        }
        response_transaction = self.basic_client.post(
            API_TRANSACTION_ITEM, data)
        self.assertEqual(200, response_transaction.status_code)
        json_transacrion_item = json.loads(
            response_transaction.content).get("message")
        self.assertEqual(json_transacrion_item, "success add category")

        transaction = Transaction.objects.get(amount=123.321)
        self.assertEqual(
            str(transaction.category.category_id),
            str(self.category1_object.category_id)
        )
        self.assertNotEqual(
            str(transaction.category.category_id),
            str(self.category2_object.category_id)
        )

    def test_user_not_auth_cannot_post_one_item_of_transaction(self):
        data = {
            "dompet": self.dompet1_object.account_id,
            "category": self.category1_object.category_id,
            "amount": 123.321
        }
        response_transaction = self.basic_client.post(
            API_TRANSACTION_ITEM, data)
        self.assertEqual(401, response_transaction.status_code)

    def test_user_auth_cant_post_transaction_if_dompet_and_category_not_found(
        self
    ):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "amount": 123.321
        }
        response_transaction = self.basic_client.post(
            API_TRANSACTION_ITEM, data)
        self.assertEqual(404, response_transaction.status_code)
