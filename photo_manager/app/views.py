from rest_framework import generics
from rest_framework import viewsets
from app.models import Photo
from app.serializer import PhotoSerializer



class PhotoListAPIView(generics.ListCreateAPIView):
    """
    View for api list
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for detail. You can go to this endpoint by "/id"
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer