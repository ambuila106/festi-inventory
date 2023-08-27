from django.http import JsonResponse
from django.urls import path, reverse, include
from rest_framework.routers import SimpleRouter

from medias.api import CategoryViewSet, MediaViewSet
router = SimpleRouter()

# /api/inventory/categories/
router.register('categories', CategoryViewSet, basename='categories')
router.register('medias', MediaViewSet, basename='products')

apiurls = ([
    path('', include(router.urls)),
    path('medias/<int:pk>/mark-as-watched/', MediaViewSet.as_view({'post': 'mark_as_watched'}), name='mark-as-watched'),
], 'medias')
