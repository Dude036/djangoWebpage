from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import utc
import datetime

# Create your models here.
class currentTime(models.Model):
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return ':',join([self.hour, self.minute, self.second,])
        