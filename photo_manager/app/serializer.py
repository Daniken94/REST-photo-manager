from .models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer is required for convert phyton code to json code
    """

    class Meta:
        model = Photo
        fields = [
            "id",
            "title",
            "albumid",
            "width",
            "height",
            "dom_colour",
            "image",
            "url",
        ]

        def create(self, data):
            return Photo.objects.create(**data)
