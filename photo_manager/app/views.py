from rest_framework import generics
from rest_framework import viewsets
from app.models import Photo
from app.serializer import PhotoSerializer



class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset






# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Photo
# from .serializer import PhotoSerializer


# @api_view(['GET'])
# def photo_list(request):
#     photos = Photo.objects.all()
#     serializer = PhotoSerializer(photos, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def photo_add(request):
#     serializer = PhotoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
