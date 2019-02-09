from django.utils import timezone
from datetime import date
from graphene.test import Client
from graphql_relay.node.node import to_global_id
from snapshottest.django import TestCase

from events.models import Event, Organization
from pycon_graphql.schemas import schema
from users.models import User
from users.tests.factories import UserFactory


class EventAPITestCase(TestCase):

    def setUp(self):
        self.client = Client(schema)

        self.main_event = Event.objects.create(
            title="Pycon 2019 - GraphQL Workshop",
            description="Descripción del evento",
            invitee_capacity=100,
            event_day=date(2019, 2, 10),
            initial_hour="13:00",
            end_hour="15:00",
            place_name="Universidad Javeriana",
            latitude='4.62844',
            longitude='-74.06508',
            zoom=19,
        )
        self.main_user = User.objects.create(
            first_name="Jhon",
            last_name="Doe",
            email="jhon@doe.com",
            profile_image="/profile/image.png",
            profile="This is the profile John Doe",
            username="jhondoe"
        )
        self.main_organization = Organization.objects.create(
            title="Python Bogotá",
            description="Python Bogotá description"
        )
        self.platform_users = UserFactory.create_batch(10)
        for user in self.platform_users:
            self.main_event.enroll_user(user)

    def test_api_events(self):
        self.assertMatchSnapshot(self.client.execute(
            '''
            query{
              events{
                edges{
                  node{
                    title
                    eventDay
                    initialHour
                    endHour
                  }
                }
              }
            }
            '''
        ))
        self.assertMatchSnapshot(self.client.execute(
            '''
            query{
              organization{
                title
                description
              }
            }
            '''
        ))

    def test_enroll_user_mutation(self):
        user_global_id = to_global_id("UserNode", self.main_user.id)
        mutation = '''
            mutation{{
              enrollUserEvent(
                eventUserInput: {{
                  eventId: "{}",
                  userId: "{}"
                }}
              ){{
                ok
                event {{
                  title
                }}
                invitee {{
                  user{{
                    email
                  }}
                }}
              }}
            }}
            '''.format(self.main_event.uuid, user_global_id)
        self.assertMatchSnapshot(self.client.execute(
            mutation
        ))

        # Invite same user again
        self.assertMatchSnapshot(self.client.execute(
            mutation
        ))

    def test_enroll_user_not_valid_mutation(self):
        user_global_id = to_global_id("UserNode", 9999)
        mutation = '''
            mutation{{
              enrollUserEvent(
                eventUserInput: {{
                  eventId: "{}",
                  userId: "{}"
                }}
              ){{
                ok
                event {{
                  title
                }}
                invitee {{
                  user{{
                    email
                  }}
                }}
              }}
            }}
            '''.format(self.main_event.uuid, user_global_id)
        self.assertMatchSnapshot(self.client.execute(
            mutation
        ))

        user_global_id = to_global_id("UserNode", self.main_user.id)
        mutation = '''
            mutation{{
              enrollUserEvent(
                eventUserInput: {{
                  eventId: "{}",
                  userId: "{}"
                }}
              ){{
                ok
                event {{
                  title
                }}
                invitee {{
                  user{{
                    email
                  }}
                }}
              }}
            }}
            '''.format("55d540ea-e708-4322-86e6-000000000000", user_global_id)
        self.assertMatchSnapshot(self.client.execute(
            mutation
        ))
