from django.contrib import admin
from .models import Photo

# Register your models here.
class photoAdmin(admin.ModelAdmin):
    list_display=['title', 'album_ID', 'width', 'height', 'dom_colour', 'image']

admin.site.register(Photo, photoAdmin)