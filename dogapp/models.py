from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
