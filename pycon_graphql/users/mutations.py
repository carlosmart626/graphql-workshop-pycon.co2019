import graphene
from django.core.validators import validate_email
from django.db import IntegrityError

from users.models import User, validate_user_email_not_exist
from users.schemas import UserNode


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    profile_image = graphene.String()
    profile = graphene.String()
    facebook_profile = graphene.String()
    twitter_profile = graphene.String()
    github_profile = graphene.String()


class RegisterUserMutation(graphene.Mutation):

    class Input:
        user_input = UserInput()

    ok = graphene.Boolean()
    user = graphene.Field(UserNode)

    @classmethod
    def mutate(cls, root, info, **input):
        ok = False
        user_data = input.get('user_input')
        try:
            validate_email(user_data.get('email'))
            validate_user_email_not_exist(user_data.get('email'))
            user = User.objects.create(**user_data)
        except IntegrityError:
            raise IntegrityError("A user already exist with the username/email provided")
        if user:
            ok = True
        return RegisterUserMutation(ok=ok, user=user)
