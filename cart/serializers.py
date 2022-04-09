from rest_framework import serializers

from cart.models import Cart, Customer, CartProduct, Order

from store.models import Product

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
        fields = ('id',)


class CartProductOnProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price_now', 'price_old', 'photo', 'discount', )


class CartProductCreateRetrieveSerializer(serializers.ModelSerializer):
    owner = CartViewOnCustomerSerializers(read_only=True)
    cart = CartViewOnCartProductSerializers(read_only=True)
    product = CartProductOnProductSerializers()
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
    owner = CartViewOnCustomerSerializers(read_only=True)
    products = CartProductCreateRetrieveSerializer(many=True)
    total_products = serializers.ReadOnlyField()
    final_price = serializers.ReadOnlyField()
    in_order = serializers.ReadOnlyField()
    for_anonymous_user = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'


class CartCreateSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer

    class Meta:
        model = Cart
        fields = ('owner',)


# -------------------------------------------------
# Order
# -------------------------------------------------


class OrderSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    cart = CartViewOnCartProductSerializers(read_only=True)

    class Meta:
        model = Order
        exclude = ('owner', 'status', )
