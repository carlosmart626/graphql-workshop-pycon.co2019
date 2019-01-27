import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from events.schemas import EventNode, InviteeNode
from users.schemas import UserNode

from users.mutations import RegisterUserMutation


class Query(graphene.ObjectType):
    event = relay.Node.Field(EventNode)
    events = DjangoFilterConnectionField(EventNode)

    invitee = relay.Node.Field(InviteeNode)
    invitees = DjangoFilterConnectionField(InviteeNode)

    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)


class Mutations(graphene.ObjectType):
    register_user = RegisterUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
