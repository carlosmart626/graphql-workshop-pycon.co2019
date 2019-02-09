import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from users.models import User


class UserNode(DjangoObjectType):
    pk = graphene.Field(type=graphene.Int, source='pk')
    exclude_fields = ('password', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )

    class Meta:
        model = User
        filter_fields = ["email", "first_name", "last_name"]
        interfaces = (relay.Node,)
