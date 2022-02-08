from tkinter import CASCADE
from django.db import models
from django.urls import reverse
class Myuser(models.Model):
    username= models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.username
class Intake(models.Model):#ORM
    id=models.AutoField(primary_key=True)
    intakename=models.CharField(max_length=30)
    startdate=models.DateField()
    enddate=models.DateField()
class Track(models.Model):
    name=models.CharField(max_length=50)
class Trainee:
    fullname=models.CharField(max_length=20)
    bdate=models.DateField()
    intakeid=models.ForeignKey('Intake',on_delete=models.CASCADE)