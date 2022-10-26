from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import PhotoViewSet


router = routers.DefaultRouter()
router.register(r'photo', PhotoViewSet, basename="queryset")

urlpatterns = [
    path('api/', include(router.urls))
]


# from .views import photo_list, photo_add

# urlpatterns = [
#     path('api/', photo_list),
#     path('api/new/', photo_add)
# ]