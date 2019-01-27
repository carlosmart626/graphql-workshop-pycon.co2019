from django.test import TestCase

from users.models import User
from users.tests.factories import UserFactory


class UserModelTestCase(TestCase):
    def setUp(self):
        self.main_user = User.objects.create(
            first_name="Jhon",
            last_name="Doe",
            email="jhon@doe.com",
            profile_image="/profile/image.png",
            profile="This is the profile John Doe",
        )

    def test_user_model(self):
        self.assertEqual(self.main_user.get_full_name(), "Jhon Doe")
        self.assertEqual(self.main_user.get_short_name(), "Jhon")

    def test_user_factory(self):
        user = UserFactory(first_name="Jhon", last_name="Doe")
        self.assertEqual(user.get_full_name(), "Jhon Doe")
        self.assertEqual(user.get_short_name(), "Jhon")
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.profile_image)
