from django.urls import path
from . import views
app_name = "users"


urlpatterns = [
    path("register/", views.register, name="register_user"),
    path("login/", views.login, name="login_user"),
    # path("info/", views.info_user, name="info_user"),
]