import graphene
from django.core.exceptions import ValidationError
from graphql_relay.node.node import from_global_id

from events.models import Event, validate_user_is_not_already_invited
from events.schemas import InviteeNode, EventNode
from users.models import User


class EnrollUserEventInput(graphene.InputObjectType):
    user_id = graphene.String(required=True)
    event_id = graphene.UUID(required=True)


class EnrollUserEventMutation(graphene.Mutation):
    class Input:
        event_user_input = EnrollUserEventInput()

    ok = graphene.Boolean()
    invitee = graphene.Field(InviteeNode)
    event = graphene.Field(EventNode)

    @classmethod
    def mutate(cls, root, info, **input):
        ok = False
        event = None
        invitee = None
        event_user_data = input.get('event_user_input')
        try:
            user_id = from_global_id(event_user_data.get('user_id'))
            event = Event.objects.get(pk=event_user_data.get('event_id'))
            user = User.objects.get(pk=user_id[1])
            validate_user_is_not_already_invited(user, event)
            invitee = event.enroll_user(user)
        except Event.DoesNotExist:
            raise ValidationError(f"Event with id {event_user_data.get('event_id')} does not exist")
        except User.DoesNotExist:
            raise ValidationError(f"User with id {event_user_data.get('user_id')} does not exist")
        if event and invitee:
            ok = True
        return EnrollUserEventMutation(ok=ok, invitee=invitee, event=event)
