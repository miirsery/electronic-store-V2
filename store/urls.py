from django.urls import path

from store.views import CategoryProductCreateAPIView, CategoryProductListAPIView, \
    ProductCreateAPIView, ProductListAPIView, CategoryProductCRUDAPIView, ProductRUDAPIView, \
    CommentCreateAPIView, CommentListAPIView, CommentRUDAPIView

urlpatterns = [
    # CATEGORY URLS
    path('categorycreated/', CategoryProductCreateAPIView.as_view()),
    path('categorylist/', CategoryProductListAPIView.as_view()),
    path('categorycrud/<int:pk>', CategoryProductCRUDAPIView.as_view()),

    # PRODUCT URLS
    path('productcreated/', ProductCreateAPIView.as_view()),
    path('productlist/', ProductListAPIView.as_view()),
    path('productrud/<int:pk>', ProductRUDAPIView.as_view()),

    # COMMENT URLS
    path('commentcreate/', CommentCreateAPIView.as_view()),
    path('commentrud/<int:pk>', CommentRUDAPIView.as_view()),
    path('comment/', CommentListAPIView.as_view()),
]
