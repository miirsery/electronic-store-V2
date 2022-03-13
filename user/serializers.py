from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'avatar',
        )

    def get_avatar(self, user):
        request = self.context.get('request',)
        avatar = user.avatar.url
        return request.build_absolute_uri(avatar)


class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('avatar',)

    def get_avatar(self, user):
        request = self.context.get('request')
        avatar = user.avatar.url
        return request.build_absolute_uri(avatar)
