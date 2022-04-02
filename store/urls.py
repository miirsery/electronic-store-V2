from django.urls import path

from store.views import CategoryProductCreateAPIView, CategoryProductListAPIView, CategoryProductDetailAPIView, \
    ProductCreateAPIView, ProductListAPIView, ProductDetailAPIView, CategoryProductCRUDAPIView, ProductCRUDAPIView

urlpatterns = [
    path('categorycreated/', CategoryProductCreateAPIView.as_view()),
    path('categorylist/', CategoryProductListAPIView.as_view()),
    path('categorydetaiel/<int:pk>', CategoryProductDetailAPIView.as_view()),
    path('categorycrud/<int:pk>', CategoryProductCRUDAPIView.as_view()),

    path('productcreated/', ProductCreateAPIView.as_view()),
    path('productlist/', ProductListAPIView.as_view()),
    path('productdetaiel/<int:pk>', ProductDetailAPIView.as_view()),
    path('productcrud/<int:pk>', ProductCRUDAPIView.as_view()),
]
