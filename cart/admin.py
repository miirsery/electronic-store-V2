from django.contrib import admin

from cart.models import Cart, CartProduct, Customer, Order


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'total_products', 'final_price', 'for_anonymous_user', 'in_order')
    list_display_links = ('owner', )
    search_fields = ('owner', 'products')
    list_filter = ('in_order', 'for_anonymous_user', )
    ordering = ('owner', )


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('owner', 'cart', 'qty', 'final_price',)
    list_display_links = ('owner', 'cart', )
    search_fields = ('owner', 'cart')
    ordering = ('owner', )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', )
    list_display_links = ('user', )
    search_fields = ('user', )
    ordering = ('user', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'first_name', 'last_name', 'phone', 'cart', 'address', 'status', 'buying_type',
                    'created_at', 'order_date')
    list_display_links = ('customer',)
    search_fields = ('customer',)
    list_filter = ('status', 'buying_type',)
