from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length=25)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    email = models.EmailField()

def __str__ (self):
    return self.name
