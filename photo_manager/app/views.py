from rest_framework import generics
from rest_framework import viewsets
from app.models import Photo
from app.serializer import PhotoSerializer



class PhotoListAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer