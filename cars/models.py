from django.db import models

# Create your models here.
class Cars(models.Model):
    make = models.CharField(max_length=25, blank=False, default='')
    model = models.CharField(max_length=25, blank=False, default='')
    year = models.IntegerField()
