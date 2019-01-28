from graphene import relay
from graphene_django import DjangoObjectType
from events.models import Event, Invitee, Organization


class OrganizationNode(DjangoObjectType):
    class Meta:
        model = Organization


class EventNode(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ["title", "event_day", "place_name"]
        interfaces = (relay.Node,)


class InviteeNode(DjangoObjectType):
    class Meta:
        model = Invitee
        filter_fields = ["user__email", "event__title", "enrolled_at", "cancelled"]
        interfaces = (relay.Node,)
