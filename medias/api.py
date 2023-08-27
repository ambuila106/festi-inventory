from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters

from rest_framework import status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from random import choice

from medias.models import Category, Media
from social.models import ViewerMedia
from medias.serializers import  CategorySerializer, MediaSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Generic Viewset to List Categories
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class MediaFilter(filters.FilterSet):
    class Meta:
        model = Media
        fields = {
            'name': ['exact', 'icontains'],
            'type': ['exact'],
            'categories__name': ['exact'],
        }

class MediaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = MediaSerializer
    ordering_fields = ['name', 'type', 'categories', 'rating']
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MediaFilter

    @action(detail=False, methods=['GET'])
    def random_media(self, request):
        random_media = choice(Media.objects.all())
        serializer = MediaSerializer(random_media)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Media.objects.all()
        ordering_param = self.request.query_params.get('ordering', 'name')

        if ordering_param == 'categories':
            queryset = queryset.order_by('categories__name')
        elif ordering_param == 'rating':
            queryset = sorted(queryset, key=lambda media: media.rating, reverse=True)
        else:
            queryset = queryset.order_by(ordering_param)

        return queryset

    @action(detail=True, methods=['POST'], permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope])
    def mark_as_watched(self, request, pk=None):
        media = self.get_object()

        viewer_media, created = ViewerMedia.objects.get_or_create(
            viewer=request.user.viewer,
            media=media
        )

        if not viewer_media.has_watched:
            viewer_media.has_watched = True
            viewer_media.save()
            return Response({'message': 'Media marked as viewed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Media is already marked as viewed'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], permission_classes=[permissions.IsAuthenticated, TokenHasReadWriteScope])
    def update_rating(self, request, pk=None):
        media = self.get_object()
        rating = request.data.get('rating')
        viewer_media, created = ViewerMedia.objects.get_or_create(
            viewer=request.user.viewer,
            media=media
        )

        viewer_media.rating= rating
        viewer_media.save()
        serializer = MediaSerializer(media)
        return Response(serializer.data)