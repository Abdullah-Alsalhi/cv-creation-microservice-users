
from django.db import models
from django.contrib.auth import validators
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        unique=True, max_length=128, null=False, verbose_name='email address')

    password = models.CharField(
        max_length=255, null=False, verbose_name='password')

    username = models.CharField(null=True, blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 16 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                max_length=16, unique=True, validators=[validators.UnicodeUsernameValidator()], verbose_name='username')

    first_name = models.CharField(
        null=True, blank=True, max_length=32, verbose_name='first name')

    last_name = models.CharField(
        null=True, blank=True, max_length=32, verbose_name='last name')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['date_joined']
