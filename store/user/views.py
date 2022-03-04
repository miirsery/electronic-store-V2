from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class UserCreateAPIView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = request.data.copy()
        data['owner'] = request.user.id
        return Response({'user_id': data['owner']})