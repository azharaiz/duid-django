from transaction.models import Transaction
from .test_base_transaction import TransactionBaseTest

EMAIL_TEST = "test@email.com"
OTHER_EMAIL_TEST = "othertest@email.com"
PASSWORD_TEST = "test12345"


class TransactionModelTest(TransactionBaseTest):

    def test_object_transaction_is_created(self):
        self.assertTrue(type(self.transaction1), Transaction)
        self.assertTrue(type(self.transaction_other), Transaction)

    def test_transaction_id_auto_generated(self):
        self.assertIsNotNone(self.transaction1.transaction_id)
        self.assertIsNotNone(self.transaction_other.transaction_id)

    def test_every_transaction_object_has_different_id(self):
        self.assertNotEqual(
            self.transaction1.transaction_id,
            self.transaction_other.transaction_id
        )

    def test_transaction1_user_is_user(self):
        self.assertEqual(self.transaction1.user, self.user)

    def test_every_transaction_object_has_different_user(self):
        self.assertNotEqual(
            self.transaction1.user, self.transaction_other.user
        )

    def test_transaction1_category_is_category1(self):
        self.assertEqual(self.transaction1.category, self.category1_object)

    def test_every_transaction_object_has_different_category(self):
        self.assertNotEqual(
            self.transaction1.category, self.transaction_other.category
        )

    def test_transaction1_dompet_is_dompet1(self):
        self.assertEqual(self.transaction1.dompet, self.dompet1_object)

    def test_every_transaction_object_has_different_dompet(self):
        self.assertNotEqual(
            self.transaction1.dompet, self.transaction_other.dompet
        )

    def test_transaction1_amount_is_100_float(self):
        self.assertEqual(self.transaction1.amount, 100.0)

    def test_every_transaction_object_has_different_amount(self):
        self.assertNotEqual(
            self.transaction1.amount, self.transaction_other.amount
        )

    def test_create_at_is_generated(self):
        self.assertEqual(
            self.transaction1.created_at, self.mocked_date
        )

    def test_updated_at_is_generated(self):
        self.assertEqual(
            self.transaction1.updated_at, self.mocked_date
        )
