from django.db import models
from django.db.models.base import Model

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    url=models.URLField(blank=True)