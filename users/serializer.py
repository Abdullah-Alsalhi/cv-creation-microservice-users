from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class SerializerUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
