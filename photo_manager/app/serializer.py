from .models import Photo
from rest_framework import serializers

# każdy model ma mieć serializer


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'album_ID', 'width', 'height', 'dom_colour']