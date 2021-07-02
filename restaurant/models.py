from django.db import models
from django.contrib.auth.models import User
#Create your models here.
class food(models.Model):
    
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()

class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return self.name