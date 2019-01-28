from django.contrib import admin
from .models import Event, Invitee, Organization


admin.site.register(Event)
admin.site.register(Invitee)
admin.site.register(Organization)
