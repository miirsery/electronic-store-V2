from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # По вот этому происходит авторизаци
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),
]