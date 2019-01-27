from graphene import relay
from graphene_django import DjangoObjectType
from users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ["email", "first_name", "last_name"]
        interfaces = (relay.Node,)
