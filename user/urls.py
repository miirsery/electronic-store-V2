from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserCreateAPIView,
    UserViewSet,
    UserUpdateView,
    UserDeleteView,
    UserUpdatePasswordView,
)


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),

    # По вот этому происходит авторизаци
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),
    path('user-auth/', UserCreateAPIView.as_view()),
    path('upload-photo/', UserUpdateView.as_view()),
    path('del-photo/', UserDeleteView.as_view()),
    path('upload-username/', UserUpdateView.as_view()),
    path('sending-key/', UserUpdateView.as_view()),
    path('key-verification/', UserUpdatePasswordView.as_view()),
]