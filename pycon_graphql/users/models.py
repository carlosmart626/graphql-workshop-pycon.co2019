from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from simplemde.fields import SimpleMDEField


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted", email="deleted@example.org")[
        0
    ]


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    profile_image = models.ImageField()
    profile = SimpleMDEField(max_length=2000, blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
