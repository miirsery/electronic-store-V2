from django.urls import path

from cart.views import CartAPIView, CartProductAPIView

urlpatterns = [
    # CART URLS
    path('mycart/<int:pk>/', CartAPIView.as_view()),
    # CART-PRODUCTS URLS
    path('produtcincart/<int:pk>/', CartProductAPIView.as_view()),
    path('produtcincart/', CartProductAPIView.as_view()),

]
