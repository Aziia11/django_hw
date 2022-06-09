from django.db import models

# Create your models here.
class Movies(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")