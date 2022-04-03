from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from store.models import Category, Product, Comment
from store.permissons import IsOwnerOrAdmin
from store.serializers import CategoryDetailSerializers, CategoryListSerializers, ProductDetailSerializers, \
    ProductListSerializer, CommentSerializers


# -------------------------------------------------
# Category Product
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
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']


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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price_now', 'status', 'discount', ]
    search_fields = ['id', 'name', ]
    ordering_fields = ['id', 'name', ]


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


# -------------------------------------------------
# Comment
# -------------------------------------------------


class CommentCreateAPIView(generics.CreateAPIView):
    """Create comment product"""

    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticated, )
    queryset = Comment.objects.filter(active=True)

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    """Retrieve Comment """

    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.filter(active=True)


class CommentUpdateAPIView(generics.UpdateAPIView):
    """ Update Comment"""

    serializer_class = CommentSerializers
    permission_classes = (IsOwnerOrAdmin,)
    queryset = Comment.objects.filter(active=True)

