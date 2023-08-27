from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, Case, When

from social.models import Viewer, ViewerMedia
from social.serializers import  ViewerSerializer, ViewerMediaSerializer


class ViewerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Generic Viewset to List Categories
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewerSerializer

    def get_queryset(self):
        queryset = Viewer.objects.all()
        return queryset


class ViewerMediaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewerMediaSerializer

    def get_queryset(self):
        queryset = ViewerMedia.objects.all()
        return queryset