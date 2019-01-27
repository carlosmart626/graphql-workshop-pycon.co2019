# Generated by Django 2.1.5 on 2019-01-27 00:11

from django.conf import settings
from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitee",
            name="user",
            field=models.ForeignKey(
                on_delete=models.SET(events.models.get_sentinel_user),
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="invitee", unique_together={("event", "user")}
        ),
    ]
