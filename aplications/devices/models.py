from __future__ import unicode_literals
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    actions = models.TextField(null=True)
    keywords = models.TextField(null=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    keywords = models.TextField(null=True)

    def __str__(self):
        return self.name
