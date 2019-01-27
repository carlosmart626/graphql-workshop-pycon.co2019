from graphene_django import DjangoObjectType
from users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
