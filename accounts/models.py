from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

#Abstract User Model
class User(AbstractUser):
    is_patient = models.BooleanField('Patient Status', default=False)
    is_consultant = models.BooleanField('Consultant Status', default=False)

#Patient Model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length = 350, default = "patient")
    age = models.IntegerField(default = 00)
    gender = models.CharField(max_length=6, default = "not-specfied")
    history = models.CharField(max_length = 500, default = "None")

    def __str__(self):
        return self.name

#Consultant Model
class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=250, default = "doctor")
    qualification = models.CharField(max_length = 100)
    speciality = models.CharField(max_length = 300)
    clinic = models.CharField(max_length = 300)
    contact = models.CharField(max_length = 13)
    email = models.EmailField(max_length = 200)
    photo = models.ImageField(upload_to = 'media', default = 'one.jpg')
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    

    

    