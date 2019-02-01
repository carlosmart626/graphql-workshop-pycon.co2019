import uuid
from django.db import models
from django.core.exceptions import ValidationError
from simplemde.fields import SimpleMDEField
from django.utils.translation import gettext_lazy as _

from users.models import User, get_sentinel_user


class Organization(models.Model):
    title = models.CharField(max_length=200)
    description = SimpleMDEField(max_length=2000, blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Organization, self).save(*args, **kwargs)


class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    invitee_capacity = models.PositiveIntegerField(default=0)
    event_day = models.DateField()
    initial_hour = models.TimeField()
    end_hour = models.TimeField()
    place_name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    latitude = models.DecimalField(default=0, max_digits=20, decimal_places=12)
    longitude = models.DecimalField(default=0, max_digits=20, decimal_places=12)
    zoom = models.PositiveSmallIntegerField(default=18)
    cover_image = models.ImageField()
    description = SimpleMDEField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def invitees(self):
        return Invitee.objects.filter(event=self, cancelled=False)

    def invitees_count(self):
        return self.invitees().count()

    def enroll_user(self, user):
        if self.invitees().filter(user=user).exists():
            raise ValidationError(f"The user {user} is already invited")
        if self.invitee_capacity == 0 or self.invitee_capacity > self.invitees_count():
            return Invitee.objects.create(event=self, user=user)


def validate_user_is_not_already_invited(user, event):
    if Invitee.objects.filter(event=event, user=user).exists():
        raise ValidationError(
            _('This user is already invited (%(value)s)'),
            params={'value': user.email},
        )


class Invitee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.SET(get_sentinel_user))
    enrolled_at = models.DateTimeField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)

    class Meta:
        unique_together = ("event", "user")
