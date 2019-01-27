import uuid
from django.db import models
from django.core.exceptions import ValidationError
from simplemde.fields import SimpleMDEField

from users.models import User, get_sentinel_user


class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = SimpleMDEField(max_length=2000, blank=True, null=True)
    invitee_capacity = models.PositiveIntegerField(default=0)
    event_day = models.DateField()
    initial_hour = models.TimeField()
    end_hour = models.TimeField()
    place_name = models.CharField(max_length=200)
    open_street_map_url = models.URLField()

    def __str__(self):
        return f"{self.title}"

    def invitees(self):
        return Invitee.objects.filter(event=self, cancelled=False)

    def invitees_count(self):
        return self.invitees().count()

    def enroll_user(self, user):
        if self.invitees().filter(user=user).exists():
            raise ValidationError(f"The user {user} is already invited")
        if self.invitee_capacity > self.invitees_count():
            return Invitee.objects.create(event=self, user=user)


class Invitee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.SET(get_sentinel_user))
    enrolled_at = models.DateTimeField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)

    class Meta:
        unique_together = ("event", "user")
