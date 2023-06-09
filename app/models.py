from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)
