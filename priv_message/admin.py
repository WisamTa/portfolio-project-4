from django.contrib import admin
from .models import Inbox, Thread, Notifications

admin.site.register(Inbox)

admin.site.register(Thread)
admin.site.register(Notifications)

