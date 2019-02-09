from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from simplemde.fields import SimpleMDEField


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted", email="deleted@example.org")[
        0
    ]


def validate_user_email_not_exist(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            _('This email is already registered (%(value)s)'),
            params={'value': value},
        )


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
        validators=[validate_user_email_not_exist, validate_email],
    )
    profile_image = models.ImageField()
    profile = SimpleMDEField(max_length=2000, blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
