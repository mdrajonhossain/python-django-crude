from django.db import models

class inserting(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    image = models.ImageField(max_length=30)



class Student(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)