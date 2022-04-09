from django.urls import path

from cart.views import CartAPIView, CartProductAPIView, OrderAPIView, CartListAPIView, CartCreateAPIView, \
    OrderCreateAPIView

urlpatterns = [
    # CART URLS
    path('cartcreate/', CartCreateAPIView.as_view()),
    path('mycart/<int:pk>/', CartAPIView.as_view()),
    path('mycart/', CartListAPIView.as_view()),
    # CART-PRODUCTS URLS
    path('produtcincart/<int:pk>/', CartProductAPIView.as_view()),
    path('produtcincart/', CartProductAPIView.as_view()),
    # ORDER
    path('order/<int:pk>/', OrderAPIView.as_view()),
    path('ordercreate/', OrderCreateAPIView.as_view()),

]
