from rest_framework import serializers
from .models import User  # note this was commented and below User model was activated when it's worked which is may raise an error in future! be aware of this error
# from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
User = get_user_model()


class SerializerUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=BaseUserManager.normalize_email(
                validated_data.get('email').lower()),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
