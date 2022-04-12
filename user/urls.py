from django.urls import path, include
from user.views import UserUpdateAPIView

urlpatterns = [
    path('api/update/<int:pk>', UserUpdateAPIView.as_view()),
]
