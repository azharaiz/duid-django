from django.test import TestCase
# Create your tests here.
from rest_framework.exceptions import ValidationError

from authentication.models import User
from target.models import Target

EMAIL_TEST_1 = "test1@email.com"
PASSWORD_TEST = "test12345"
MOCK_TARGET_TITLE_1 = "mock_target_title_1"
MOCK_TARGET_TITLE_2 = "mock_target_title_2"
MOCK_TARGET_AMOUNT_1 = 1000
MOCK_TARGET_AMOUNT_2 = 20000
MOCK_TARGET_DATE_1 = '2020-12-30'
MOCK_TARGET_DATE_2 = '2020-12-28'


class TargetModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_superuser(email=EMAIL_TEST_1, password=PASSWORD_TEST)

        Target(target_title=MOCK_TARGET_TITLE_1, target_amount=MOCK_TARGET_AMOUNT_1,
               user=self.user1, due_date=MOCK_TARGET_DATE_1).save()
        Target(target_title=MOCK_TARGET_TITLE_2, target_amount=MOCK_TARGET_AMOUNT_2,
               user=self.user1, due_date=MOCK_TARGET_DATE_2).save()
        self.all_target = Target.objects.all()

    def test_target_can_be_created(self):
        self.assertEqual(len(self.all_target), 2)
        self.assertNotEqual(self.all_target[0], self.all_target[1])
        self.assertEqual(self.all_target[0].target_title, MOCK_TARGET_TITLE_1)
        self.assertEqual(self.all_target[1].target_title, MOCK_TARGET_TITLE_2)
        self.assertEqual(self.all_target[0].target_amount, MOCK_TARGET_AMOUNT_1)
        self.assertEqual(self.all_target[1].target_amount, MOCK_TARGET_AMOUNT_2)
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
        self.assertEqual(Target.objects.get(target_id=test_obj.target_id).target_title, MOCK_TARGET_TITLE_2)
        self.assertEqual(Target.objects.get(target_id=test_obj.target_id).target_amount, MOCK_TARGET_AMOUNT_2)
        self.assertEqual(str(Target.objects.get(target_id=test_obj.target_id).due_date), MOCK_TARGET_DATE_2)
        self.assertEqual(2, len(Target.objects.all()))

    def test_target_can_be_deleted(self):
        self.assertEqual(2, len(self.all_target))
        Target.objects.all().delete()
        self.assertEqual(0, len(Target.objects.all()))

    def test_target_cant_be_less_than_0(self):
        new_test_target = Target(due_date=MOCK_TARGET_DATE_1, target_title=MOCK_TARGET_TITLE_1,
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
