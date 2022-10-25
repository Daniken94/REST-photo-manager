from rest_framework import generics
from rest_framework import viewsets
from app.models import Photo
from app.serializer import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
