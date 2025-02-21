from django.db import models



class students(models.Model):
    ad_no=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    mail=models.TextField()
    cls=models.IntegerField()
    subject=models.TextField()



