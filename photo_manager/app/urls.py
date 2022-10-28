from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import PhotoListAPIView, PhotoDetailAPIView


urlpatterns = [
    path("", PhotoListAPIView.as_view(), name="list_create_view"),
    path("<int:pk>/", PhotoDetailAPIView.as_view(), name="details"),
]
