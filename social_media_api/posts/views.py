from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission: only owners can edit/delete"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ["author__username"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get posts from users the current user follows
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


class LikeToggleView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            # If already liked → unlike it
            like.delete()
            return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)

        # If newly liked → create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id,
            )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)
