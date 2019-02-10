import django_filters
import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from users.models import User


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = {
            'username': ['exact', 'contains'],
            'first_name': ['iexact', 'contains'],
            'last_name': ['iexact', 'contains'],
        }

    @property
    def qs(self):
        # The query context can be found in self.request.
        if self.request.user.is_authenticated:
            return super(UserFilter, self).qs
        return User.objects.none()


class UserNode(DjangoObjectType):
    pk = graphene.Field(type=graphene.Int, source='pk')
    exclude_fields = ('password', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )

    class Meta:
        model = User
        filter_fields = ["email", "first_name", "last_name"]
        interfaces = (relay.Node,)
