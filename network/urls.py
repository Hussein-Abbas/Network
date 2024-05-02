
from django.urls import path

from . import views

urlpatterns = [
    path("<int:page_number>", views.index, name="index"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("follow", views.follow, name="follow"),
    path("following/<int:page_number>", views.following, name="following"),
    path("following", views.following, name="following"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("like", views.like, name="like"),
    path("<str:username>/<int:page_number>/", views.profile, name="profile"),
    path("<str:username>/", views.profile, name="profile"),
]
