import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from events.schemas import EventNode, InviteeNode, OrganizationNode
from users.schemas import UserNode

from events.models import Organization

from users.mutations import RegisterUserMutation
from events.mutations import EnrollUserEventMutation


class Query(graphene.ObjectType):
    organization = graphene.Field(OrganizationNode)

    event = relay.Node.Field(EventNode)
    events = DjangoFilterConnectionField(EventNode)

    invitee = relay.Node.Field(InviteeNode)
    invitees = DjangoFilterConnectionField(InviteeNode)

    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    def resolve_organization(self, info):
        return Organization.objects.get(pk=1)


class Mutations(graphene.ObjectType):
    register_user = RegisterUserMutation.Field()
    enroll_user_event = EnrollUserEventMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
