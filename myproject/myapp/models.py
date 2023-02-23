from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100,null=True)
    details = models.CharField(max_length=500,null=True)

class Register(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    password2 = models.CharField(max_length=100,null=True)