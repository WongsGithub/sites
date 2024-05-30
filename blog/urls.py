from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("sign", views.sign, name="sign"),
    path("login", views.login, name="login"),
]