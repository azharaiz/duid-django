from transaction.models import Transaction
from category.util import UtilCategory
from .test_base_transaction import TransactionBaseTest


EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"
API_TRANSACTION_ITEM = "/api/transaction/"


class TransactionItemViewTest(TransactionBaseTest):

    def test_user_auth_can_delete_one_item_of_transaction(self):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_transaction = self.client.generic(
            method="DELETE",
            path=API_TRANSACTION_ITEM +
            str(self.transaction1.transaction_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(200, response_transaction.status_code)

    def test_user_not_auth_cannot_delete_one_item_of_transaction(self):
        response_transaction = self.client.generic(
            method="DELETE",
            path=API_TRANSACTION_ITEM +
            str(self.transaction1.transaction_id) + "/",
            content_type='application/json'
        )
        self.assertNotEqual(200, response_transaction.status_code)
        self.assertEqual(401, response_transaction.status_code)

    def test_user_auth_cannot_delete_one_transaction_if_id_wrong_or_null(
        self
    ):
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_transaction = self.client.generic(
            method="DELETE",
            path=API_TRANSACTION_ITEM +
            str(self.transaction1.category.category_id) + "/",
            content_type='application/json'
        )
        self.assertEqual(404, response_transaction.status_code)

    def test_user_auth_can_put_one_item_of_transaction(self):
        transaction1_id = str(self.transaction1.transaction_id)
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "dompet": self.dompet1_object.account_id,
            "category": self.category1_object.category_id,
            "amount": 123.321
        }
        response_transaction = self.basic_client.put(
            API_TRANSACTION_ITEM + transaction1_id + "/",
            data, content_type="application/json"
        )
        self.assertEqual(200, response_transaction.status_code)

        transaction = Transaction.objects.get(amount=123.321)
        self.assertEqual(
            str(transaction.category.category_id),
            str(self.category1_object.category_id)
        )

    def test_user_not_auth_cannot_post_one_item_of_transaction(self):
        transaction1_id = str(self.transaction1.transaction_id)
        data = {
            "dompet": self.dompet1_object.account_id,
            "category": self.category1_object.category_id,
            "amount": 123.321
        }
        response_transaction = self.basic_client.put(
            API_TRANSACTION_ITEM + transaction1_id + "/",
            data, content_type="application/json"
        )
        self.assertEqual(401, response_transaction.status_code)

    def test_user_auth_cant_post_transaction_if_dompet_and_category_not_found(
        self
    ):
        transaction1_id = str(self.transaction1.transaction_id)
        token = UtilCategory.get_jwt_token(
            self.client, EMAIL_TEST, PASSWORD_TEST)
        self.basic_client.defaults["HTTP_AUTHORIZATION"] = 'Bearer ' + token
        data = {
            "amount": 123.321
        }
        response_transaction = self.basic_client.put(
            API_TRANSACTION_ITEM + transaction1_id + "/",
            data, content_type="application/json"
        )
        self.assertEqual(200, response_transaction.status_code)
