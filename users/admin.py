from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User
# Register your models here.

# not worked on admin yet


class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'email', 'username', 'is_active']


admin.site.register(User, UserAdmin)
