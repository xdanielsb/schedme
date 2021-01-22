from django.contrib import admin

from .models import FreeTime, Hobbie, Activity, CalendarCredentials

admin.site.register(FreeTime)
admin.site.register(Hobbie)
admin.site.register(Activity)
admin.site.register(CalendarCredentials)
