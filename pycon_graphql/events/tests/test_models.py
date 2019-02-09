from django.core.exceptions import ValidationError
from django.utils import timezone
from django.test import TestCase
from events.models import Event, Invitee
from users.tests.factories import UserFactory
from users.models import get_sentinel_user


class EventModelTestCase(TestCase):
    def setUp(self):
        self.main_event = Event.objects.create(
            title="Pycon 2019 - GraphQL Workshop",
            description="Descripción del evento",
            invitee_capacity=100,
            event_day=timezone.now().date(),
            initial_hour="13:00",
            end_hour="15:00",
            place_name="Universidad Javeriana",
            latitude='4.62844',
            longitude='-74.06508',
            zoom=19,
        )
        self.platform_users = UserFactory.create_batch(10)
        for user in self.platform_users:
            self.main_event.enroll_user(user)

    def test_event_model(self):
        self.assertEqual(str(self.main_event), "Pycon 2019 - GraphQL Workshop")
        self.assertEqual(self.main_event.invitees_count(), 10)

        self.assertEqual(Invitee.objects.filter(event=self.main_event).count(), 10)

    def test_error_already_enrolled_user(self):
        user = self.platform_users[0]
        with self.assertRaises(ValidationError):
            self.main_event.enroll_user(user)

    def test_delete_enrolled_user(self):
        new_user = UserFactory()
        invitee = self.main_event.enroll_user(new_user)
        new_user.delete()
        invitee.refresh_from_db(fields=("user",))
        self.assertEqual(invitee.user, get_sentinel_user())
