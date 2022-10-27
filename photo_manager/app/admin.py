from django.contrib import admin
from .models import Photo

# Register your models here.
class photoAdmin(admin.ModelAdmin):
    list_display=['title', 'albumid', 'width', 'height', 'dom_colour', 'image', 'url']

admin.site.register(Photo, photoAdmin)