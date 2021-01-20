from django.db import models
from django.contrib.auth.models import User


class FreeTime(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    day = models.DateField()

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.start, self.end, self.day, self.student.name
        )


class Hobbie(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {} ".format(self.name, self.student)
