from django.db import models
from ..common import calendar

class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    credentials = models.TextField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.name, self.email)
    
    def getCredentials(self):
        """
        Obtain the user token from the database, generating it if it does not exist
        """
        # TODO : store credentials as Text, here they are objects
        self.token = calendar.refresh_creds(self.token)
        self.save()
        return self.token


class FreeTime(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    day = models.DateField()

    def __str__(self):
        return "{} - {} - {} - {}".format(self.start, self.end, self.day, self.student.name)


class Hobbie(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {} ".format(self.name, self.student.name)
