from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from store.models import Category, Product
from store.serializers import CategoryDetailSerializers, CategoryListSerializers, ProductDetailSerializers, \
    ProductListSerializer


# -------------------------------------------------
# Category
# -------------------------------------------------


class CategoryProductCreateAPIView(generics.CreateAPIView):
    """ Make Category Product """

    serializer_class = CategoryDetailSerializers
    permission_classes = (IsAdminUser,)


class CategoryProductListAPIView(generics.ListAPIView):
    """ View Category Product List """

    serializer_class = CategoryListSerializers
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)


class CategoryProductDetailAPIView(generics.RetrieveAPIView):
    """ View Category Product Detail """

    serializer_class = CategoryDetailSerializers
    queryset = Category
    permission_classes = (AllowAny,)


class CategoryProductCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ CRUD Category Product """

    serializer_class = CategoryDetailSerializers
    queryset = Category
    permission_classes = (IsAdminUser,)

# -------------------------------------------------
# Product
# -------------------------------------------------


class ProductCreateAPIView(generics.CreateAPIView):
    """ Make  Product"""

    serializer_class = ProductDetailSerializers
    permission_classes = (IsAdminUser,)


class ProductListAPIView(generics.ListAPIView):
    """ View Product List"""

    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)


class ProductDetailAPIView(generics.RetrieveAPIView):
    """ View Product Detail """

    serializer_class = ProductDetailSerializers
    queryset = Product
    permission_classes = (AllowAny,)


class ProductCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ CRUD Product """

    serializer_class = ProductDetailSerializers
    queryset = Product
    permission_classes = (IsAdminUser,)


