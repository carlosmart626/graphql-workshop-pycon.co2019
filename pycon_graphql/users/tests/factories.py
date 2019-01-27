import factory
from django.utils.text import slugify

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(
        lambda o: slugify(o.first_name + "." + o.last_name)
    )
    email = factory.LazyAttribute(
        lambda a: "{0}.{1}@example.com".format(a.first_name, a.last_name).lower()
    )
