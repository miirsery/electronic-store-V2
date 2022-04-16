from rest_framework import serializers

from sendemail.models import CustomerLetters
from user.models import User


class UserSerializerOnCustomerLetters(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'status', 'phone', 'address',)


class CustomerLettersSerializer(serializers.ModelSerializer):

    user = UserSerializerOnCustomerLetters(read_only=True)

    class Meta:
        model = CustomerLetters
        fields = ('subject', 'message', 'attachments', 'user')
