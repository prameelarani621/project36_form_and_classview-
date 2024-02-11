from django.db import models

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100)
    sprincepal=models.CharField(max_length=100)