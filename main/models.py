from django.db import models

# Create your models here.

class myModel(models.Model):
    field = models.CharField(max_length=100)