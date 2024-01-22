from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters

from rest_framework import status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from random import choice

from rest_framework import generics
from main.serializers import UserRegistrationSerializer


class UserRegistrationViewSet(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer