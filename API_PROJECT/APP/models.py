from django.db import models

# Create your models here.
class student(models.Model):
    name=models.TextField()
    roll=models.IntegerField()
    place=models.TextField()

    def __str__(self):
        return self.name  # to show the names of students instead of object1,object2,etc