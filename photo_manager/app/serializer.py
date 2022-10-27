from .models import Photo
from rest_framework import serializers

# każdy model ma mieć serializer


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'albumid', 'width', 'height', 'dom_colour', 'image', 'url']

        def create(self, data):
            return Photo.objects.create(**data)
