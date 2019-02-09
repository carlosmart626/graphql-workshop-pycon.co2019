import graphene
import graphql_jwt
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from events.models import Organization
from events.mutations import EnrollUserEventMutation
from events.schemas import EventNode, InviteeNode, OrganizationNode
from users.models import User
from users.mutations import RegisterUserMutation, LoginUser, LogoutUser
from users.schemas import UserNode


class Query(graphene.ObjectType):
    organization = graphene.Field(OrganizationNode)

    event = relay.Node.Field(EventNode)
    events = DjangoFilterConnectionField(EventNode)

    invitee = relay.Node.Field(InviteeNode)
    invitees = DjangoFilterConnectionField(InviteeNode)

    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    me = graphene.Field(UserNode)

    def resolve_organization(self, info):
        return Organization.objects.get(pk=1)

    def resolve_users(self, info):
        # context will reference to the Django request
        if not info.context.user.is_authenticated():
            return User.objects.none()
        else:
            return User.objects.all()

    @login_required
    def resolve_me(self, info):
        return UserNode.get_node(info, info.context.user.id)


class Mutations(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register_user = RegisterUserMutation.Field()
    login_user = LoginUser.Field()
    logout_user = LogoutUser.Field()


class PrivateMituations(graphene.ObjectType):
    enroll_user_event = EnrollUserEventMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

private_schema = graphene.Schema(query=Query, mutation=PrivateMituations)
