from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length= 20)

    def __str__(self):
        return self.name

class Device(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    storage = models.IntegerField()
    ram = models.IntegerField()
    colour = models.CharField(max_length=20)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)

class Enquiry(models.Model):
    firstname = models.CharField(max_length=50, blank=True, null=True)
    secondname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    phonetype= models.CharField(max_length=100)
    damage = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.phonenumber