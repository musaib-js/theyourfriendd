from functools import partialmethod
from django.db import models
from accounts.models import Consultant, User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title  = models.CharField(max_length = 300)
    author = models.CharField(max_length = 300)
    body = models.TextField()
    timeStamp = models.DateTimeField()
    slug = models.CharField(max_length = 350)
    tags = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

class Appointment(models.Model):
    name = models.CharField(max_length = 250)
    gender = models.CharField(max_length = 7)
    concern = models.CharField(max_length = 300)
    description = models.TextField()
    doctor = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    appointmentdate = models.CharField(max_length = 25)

    def __str__(self):
        return self.name + " on " + self.appointmentdate
    
    
