
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(default="https://miro.medium.com/max/720/1*W35QUSvGpcLuxPo3SRTH4w.png")
    firstname = models.CharField(max_length=128, null=False)
    lastname = models.CharField(max_length=128, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    phone = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=128, null=False)