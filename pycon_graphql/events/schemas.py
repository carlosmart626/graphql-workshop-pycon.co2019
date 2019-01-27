from graphene_django import DjangoObjectType
from events.models import Event, Invitee


class EventNode(DjangoObjectType):
    class Meta:
        model = Event


class InviteeNode(DjangoObjectType):
    class Meta:
        model = Invitee
