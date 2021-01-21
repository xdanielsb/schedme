from django.db import models
from django.contrib.auth.models import User


class FreeTime(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return "{} - {} - {}".format(
            self.start, self.end, self.student
        )

    @property
    def get_start(self):
        return self.start.strftime("%m/%d/%Y %H:%M %p")

    @property
    def get_end(self):
        return self.end.strftime("%m/%d/%Y %H:%M %p")


class Hobbie(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {} ".format(self.name, self.student)
