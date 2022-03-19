from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserSerializer,
    UserUpdateSerializer,
)
from .models import User
from rest_framework import status
from django.conf import settings

import os


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class UserCreateAPIView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = request.data.copy()
        return Response(UserSerializer(request.user, context={"request":request}).data)


class UserUpdateView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(request.user, request.data)
            return Response(UserUpdateSerializer(request.user, context={"request": request}).data, status.HTTP_200_OK)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(request.user, request.data)
            return Response(UserSerializer(request.user, context={"request": request}).data, status.HTTP_200_OK)

class UserDeleteView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        user.avatar = 'avatars/Алакшин.jpg'
        user.save()
        return Response(UserSerializer(user, context={"request": request}).data, status.HTTP_200_OK)
