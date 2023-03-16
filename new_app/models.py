from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField
    users = models.CharField(max_length=64)


class TODO(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField
    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    user = models.CharField(max_length=64)
    on_off = models.BooleanField
