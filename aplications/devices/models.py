from __future__ import unicode_literals
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    actions = models.TextField(null=True)
