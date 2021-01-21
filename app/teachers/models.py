from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    url_video_call = models.CharField(max_length=2000)
    student = models.ForeignKey(
        User, editable=False, null=True, on_delete=models.SET_NULL
    )
    topic = models.CharField(max_length=30)
    start = models.TimeField()
    end = models.TimeField()
    day = models.DateField()

    def __str__(self):
        return "{}".format(self.topic)
