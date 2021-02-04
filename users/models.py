from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.TextField(default='null')
    email = models.TextField(default='null')
    price = models.IntegerField()
