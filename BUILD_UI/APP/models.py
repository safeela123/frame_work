from django.db import models
from django.utils import timezone


# Create your models here.
class ui(models.Model):
    text=models.TextField()
    date = models.DateField(auto_now=True)
