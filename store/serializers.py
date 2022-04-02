from rest_framework import serializers

from store.models import Category, Product


# -------------------------------------------------
# Category Product List and Detail
# -------------------------------------------------

class CategoryListSerializers(serializers.ModelSerializer):
    """ Category Product List """

    class Meta:
        model = Category
        fields = ('id', 'name', 'description',)


class CategoryDetailSerializers(serializers.ModelSerializer):
    """ Category Product Detail """

    class Meta:
        model = Category
        fields = '__all__'


# -------------------------------------------------
# Product List and Detail
# -------------------------------------------------


class ProductListSerializer(serializers.ModelSerializer):
    """ Product List """

    class Meta:
        model = Product
        fields = ('id', 'name', 'price_now', 'quantity', 'photo', 'status', 'specifications', 'cat')


class ProductDetailSerializers(serializers.ModelSerializer):
    """ Product Detail """
    class Meta:
        model = Product
        fields = '__all__'
