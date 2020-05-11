from rest_framework import serializers

from django.contrib.auth.models import User
from newsfeed.models import Post, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all())
    comments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Comment.objects.all())
    likes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Like.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'likes']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'photo', 'description']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'owner', 'post']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['owner', 'post']
