from rest_framework import serializers

from social.models import Viewer, ViewerMedia


class ViewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Viewer
        fields = ['id', 'user']


class ViewerMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewerMedia
        fields = ['id','Viewer']
