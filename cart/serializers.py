from rest_framework import serializers

from cart.models import Cart, Customer, CartProduct


# -------------------------------------------------
# Customer
# -------------------------------------------------

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# -------------------------------------------------
# CartProduct
# -------------------------------------------------


class CartViewOnCustomerSerializers(serializers.ModelSerializer):
    """ Serializers Customer for CartProductCreateRetrieveSerializer"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Customer
        fields = ('user',)


class CartViewOnCartProductSerializers(serializers.ModelSerializer):
    """ Serializers Cart for CartProductCreateRetrieveSerializer"""
    class Meta:
        model = Cart
        fields = ('cart',)


class CartProductCreateRetrieveSerializer(serializers.ModelSerializer):
    owner = CartViewOnCustomerSerializers(read_only=True)
    cart = CartViewOnCartProductSerializers
    final_price = serializers.ReadOnlyField()

    class Meta:
        model = CartProduct
        fields = ('owner', 'cart', 'product', 'qty', 'final_price',)


class CartProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('qty',)


# -------------------------------------------------
# Cart
# -------------------------------------------------

class CartSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer
    products = CartProductCreateRetrieveSerializer(many=True)
    total_products = serializers.ReadOnlyField()
    final_price = serializers.ReadOnlyField()
    in_order = serializers.ReadOnlyField()
    for_anonymous_user = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'
