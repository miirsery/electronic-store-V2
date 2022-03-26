from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserSerializer,
    UserUpdateSerializer,
    UserEmailSerializer,
    # UserPasswordUpdateSerializer,
)
from .models import User
from rest_framework import status
from django.conf import settings

import os
import secrets
import string
import hashlib


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
    
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UserEmailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            random_string = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
            send_mail(
                'Test',
                f'{random_string} - ваш ключ для смены пароля',
                'griga2888@mail.ru',
                ['griga2888@mail.ru'],
                fail_silently=False,
            )
            user.password_change_key = random_string
            user.save()
            return Response(UserEmailSerializer(user, context={"request": random_string}).data, status.HTTP_200_OK)

class UserDeleteView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        user.avatar = 'avatars/defalt.jpg'
        user.save()
        return Response(UserSerializer(user, context={"request": request}).data, status.HTTP_200_OK)

class UserUpdatePasswordView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.user.password_change_key == request.data['password_change_key']:
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})

    def patch(self, request, *args, **kwargs):
        # serializer = UserPasswordUpdateSerializer(request.user, data=request.data, partial=True)
        # if serializer.is_valid():
        request.user.set_password(request.data['password'])
        request.user.save()
        return JsonResponse({'replaced': True})
