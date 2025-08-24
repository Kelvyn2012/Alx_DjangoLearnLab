from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView, LikeToggleView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="user-feed"),
    path("posts/<int:pk>/like-toggle/", LikeToggleView.as_view(), name="like-toggle"),
]
