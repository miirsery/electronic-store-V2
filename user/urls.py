from django.urls import path, include
from user.views import UserUpdateAPIView

urlpatterns = [
    path('api/update', UserUpdateAPIView.as_view()),
]
