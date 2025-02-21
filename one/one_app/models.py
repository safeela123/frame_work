from django.db import models

# Create your models here.
class students(models.Model):
    ad_no=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.TextField()
    cls=models.IntegerField()
    subject=models.TextField()
