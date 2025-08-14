# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    profile_view,
    edit_profile_view,
    PostCreateView,
    PostDeleteView,
    PostListView,
    PostUpdateView,
    PostDetailView,
)

urlpatterns = [
    path("register/", register_view, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", edit_profile_view, name="edit_profile"),
    path("", PostListView.as_view(), name="post-list"),  # /
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # post/1/
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # post/new/
    path(
        "post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"
    ),  # post/1/update/
    path(
        "post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"
    ),  # post/1/delete/
]
