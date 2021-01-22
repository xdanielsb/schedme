from django.urls import path

from . import views

app_name = "teachers"

urlpatterns = [
    path("generate_test", views.generate_test_teachers, name="generate_test"),
    path("", views.index, name="all"),
    path("<int:id>", views.desc, name="desc_teacher"),
]
