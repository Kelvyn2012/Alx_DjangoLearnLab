from rest_framework import serializers
from .models import Post, Comment, Tag


# Serialize Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


# Serialize Comment
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Shows username instead of ID

    class Meta:
        model = Comment
        fields = "__all__"


# Serialize Post with nested comments & tags
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Related name = "comments"
    tags = TagSerializer(many=True, read_only=True)  # For Tag model

    class Meta:
        model = Post
        fields = "__all__"
