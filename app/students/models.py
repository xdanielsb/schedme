from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.name, self.email)


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
