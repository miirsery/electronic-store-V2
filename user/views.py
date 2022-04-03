from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """ User Update View"""

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
