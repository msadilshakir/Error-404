from django.db import models

# Create your models here.

class contactform(models.Model):
    first_name = models.CharField(max_length=100)
    email =models.EmailField()
    comments=models.TextField()