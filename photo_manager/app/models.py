from email.policy import default
from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=120)
    album_ID = models.IntegerField(default=1)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    dom_colour = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="photos", height_field='height', width_field='width')

    def __str__(self):
            return f"{self.title}"


