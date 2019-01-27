import graphene

from users.schemas import UserNode
from users.models import User


class Query(graphene.ObjectType):
    all_users = graphene.List(UserNode)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()


schema = graphene.Schema(query=Query)
