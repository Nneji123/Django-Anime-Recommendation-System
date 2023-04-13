from django.db import models

# Create your models here.

class Anime(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.URLField()
    description = models.TextField()
    
