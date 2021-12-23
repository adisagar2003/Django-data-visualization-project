from django.db import models

# Create your models here.

class Posts(models.Model):
    text = models.TextField()
    aditya = models.CharField(max_length=1000)



