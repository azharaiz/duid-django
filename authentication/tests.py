from django.test import TestCase

from authentication.models import User

EMAIL_TEST = "test@email.com"


class UserManagerTest(TestCase):
    def test_user_create_success(self):
        user = User.objects.create_user(email=EMAIL_TEST)
        self.assertEqual(user.email, EMAIL_TEST)

    def test_user_create_fail(self):
        with self.assertRaises(TypeError):
            user = User.objects.create_user()
            self.assertEqual(user.email, None)


class UserModelTest(TestCase):
    def test_user_save_success(self):
        user = User()
        user.email = EMAIL_TEST
        user.save()

        self.assertEqual(user.email, EMAIL_TEST)

    def test_user_save_fail(self):
        with self.assertRaises(ValueError):
            user = User()
            user.save()

            self.assertEqual(user.email, None)
