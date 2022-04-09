from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartProduct, Customer, Order
from cart.permission import IsOwner, IsOwnerOrAdmin
from cart.serializers import CartSerializer, CartProductCreateRetrieveSerializer, CartProductUpdateSerializer, \
    OrderSerializerRetrieve, CartCreateSerializer, OrderCreateSerializer


class CartCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        Customer.objects.get_or_create(user=request.user, phone=request.user.phone,
                                       address=request.user.address)
        serializer = CartCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = Customer.objects.get(user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartAPIView(generics.RetrieveAPIView):
    """ Cart Retrieve"""
    queryset = Cart.objects.all()
    permission_classes = (IsOwner,)
    serializer_class = CartSerializer


class CartListAPIView(generics.ListAPIView):
    """ Cart List"""
    queryset = Cart.objects.all()
    permission_classes = (IsOwnerOrAdmin,)
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['in_order', 'for_anonymous_user', ]


class CartProductAPIView(APIView):
    """CRUD CartProduct. An instance is created for each cart product in the Cart product table"""

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            serializer = CartProductCreateRetrieveSerializer(CartProduct.objects.all(), many=True)
        else:
            serializer = CartProductCreateRetrieveSerializer(CartProduct.objects.filter(pk=kwargs['pk']), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CartProductCreateRetrieveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = Customer.objects.get(user=request.user)
            serializer.validated_data['cart'] = Cart.objects.get(owner__user=request.user, in_order=False)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        serializer = CartProductUpdateSerializer(CartProduct.objects.filter(pk=kwargs['pk']).first(), data=request.data)
        if kwargs.get('pk') is not None:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise AssertionError("Expected view CartProductAPIView to be called with a URL keyword argument named "
                                 "'pk' if the method is called 'PUT' ")

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            CartProduct.objects.filter(pk=kwargs['pk']).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise AssertionError("Expected view CartProductAPIView to be called with a URL keyword argument named "
                                 "'pk' if the method is called 'DELETE' ")


class OrderAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsOwnerOrAdmin,)
    serializer_class = OrderSerializerRetrieve


class OrderCreateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = Customer.objects.get(user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

