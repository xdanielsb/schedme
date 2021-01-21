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

class Activity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    isLocal = models.BooleanField(default=True) # true when the activity is scheduled by our software
    google_id = models.IntegerField()

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

class CalendarCredentials(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    credentials = models.BinaryField()

    def __str__(self) -> str:
        return self.student

class Hobbie(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {} ".format(self.name, self.student)
