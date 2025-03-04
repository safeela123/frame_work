from django.db import models


# Create your models here.
class forms(models.Model):
    roll=models.IntegerField()
    name=models.TextField()
    mark=models.IntegerField()
    