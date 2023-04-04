from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=70, unique=True)
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)