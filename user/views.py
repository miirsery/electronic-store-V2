from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Customer
from user.models import User
from user.permissions import IsOwner
from user.serializers import UserSerializer


class UserUpdateAPIView(APIView):
    """ User Update View"""

    permission_classes = (IsOwner, )

    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.filter(pk=kwargs['pk']).first(), data=request.data, partial=True)
        if kwargs.get('pk') is not None:
            if serializer.is_valid():
                serializer.save()
                customer = Customer.objects.get(user=request.user)
                customer.update()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise AssertionError("Expected view CartProductAPIView to be called with a URL keyword argument named "
                                 "'pk' if the method is called 'PUT' ")


