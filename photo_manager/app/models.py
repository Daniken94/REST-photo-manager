from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=120)
    album_ID = models.IntegerField
    width = models.IntegerField
    height = models.IntegerField
    dom_colour = models.IntegerField