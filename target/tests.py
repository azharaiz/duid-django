from django.test import TestCase

# Create your tests here.
from authentication.models import User
from target.models import Target

EMAIL_TEST_1 = "test1@email.com"
PASSWORD_TEST = "test12345"


class TargetModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_superuser(email=EMAIL_TEST_1, password=PASSWORD_TEST)
        self.mock_target_title_1 = "mock_target_title_1"
        self.mock_target_title_2 = "mock_target_title_2"
        self.mock_target_amount_1 = 1000
        self.mock_target_amount_2 = 20000
        self.mock_target_date_1 = '2020-12-30'
        self.mock_target_date_2 = '2020-12-28'

        Target(target_title=self.mock_target_title_1, target_amount=self.mock_target_amount_1,
               user=self.user1, due_date=self.mock_target_date_1).save()
        Target(target_title=self.mock_target_title_2, target_amount=self.mock_target_amount_2,
               user=self.user1, due_date=self.mock_target_date_2).save()
        self.all_target = Target.objects.all()

    def test_target_can_be_created(self):
        self.assertEqual(len(self.all_target), 2)
        self.assertNotEqual(self.all_target[0], self.all_target[1])
        self.assertEqual(self.all_target[0].target_title, self.mock_target_title_1)
        self.assertEqual(self.all_target[1].target_title, self.mock_target_title_2)
        self.assertEqual(self.all_target[0].target_amount, self.mock_target_amount_1)
        self.assertEqual(self.all_target[1].target_amount, self.mock_target_amount_2)
        self.assertEqual(self.all_target[0].user, self.user1)
        self.assertEqual(self.all_target[1].user, self.user1)
        self.assertEqual(str(self.all_target[0].due_date), self.mock_target_date_1)
        self.assertEqual(str(self.all_target[1].due_date), self.mock_target_date_2)

    def test_target_can_be_updated(self):
        self.assertEqual(2, len(self.all_target))
        test_obj = self.all_target[0]
        self.assertNotEqual(test_obj.target_title, self.mock_target_title_2)
        test_obj.target_title = self.mock_target_title_2
        test_obj.target_amount = self.mock_target_amount_2
        test_obj.due_date = self.mock_target_date_2
        test_obj.save()
        self.assertEqual(Target.objects.get(target_id=test_obj.target_id).target_title, self.mock_target_title_2)
        self.assertEqual(Target.objects.get(target_id=test_obj.target_id).target_amount, self.mock_target_amount_2)
        self.assertEqual(str(Target.objects.get(target_id=test_obj.target_id).due_date), self.mock_target_date_2)
        self.assertEqual(2, len(Target.objects.all()))

    def test_target_can_be_deleted(self):
        self.assertEqual(2, len(self.all_target))
        Target.objects.all().delete()
        self.assertEqual(0, len(Target.objects.all()))
