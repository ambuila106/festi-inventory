from django.http import JsonResponse
from django.urls import path, reverse, include
from rest_framework.routers import SimpleRouter

from social.api import ViewerViewSet, ViewerMediaViewSet
router = SimpleRouter()

# /api/inventory/categories/
router.register('viewers', ViewerViewSet, basename='viewers')
router.register('viewers', ViewerMediaViewSet, basename='viewers-media')


apiurls = ([
    path('', include(router.urls)),
], 'medias')
