from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class Log(models.Model):
    date = models.DateField('Fecha', default=datetime.now)
    type = models.CharField(max_length=100)
    text = models.TextField(null=True)