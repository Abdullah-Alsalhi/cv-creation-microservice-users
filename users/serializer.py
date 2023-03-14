from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo

class SerializerUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class SerializerUserInfo(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'