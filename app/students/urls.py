from django.urls import path

from . import views

app_name = "students"

urlpatterns = [
    path("", views.index, name="index"),
    path("guest", views.guest, name="guest"),
    path("load_calendar", views.load_calendar, name="load"),
    path("save_hobbies", views.save_hobbies, name="save_hobbies"),
    path("generate_calendar", views.generate_plan, name="generate_calendar"),
    path("save_event", views.save_event, name="save_event"),
    path("logout", views.logouts),
]
