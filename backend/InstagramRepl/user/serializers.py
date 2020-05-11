from rest_framework import serializers

from django.contrib.auth.models import User
from user.models import Profile
from newsfeed.models import Post, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    profiles = serializers.PrimaryKeyRelatedField(many= True, queryset = Profile.objects.all())
    posts = serializers.PrimaryKeyRelatedField(many= True, queryset = Post.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many= True, queryset = Comment.objects.all())
    likes = serializers.PrimaryKeyRelatedField(many= True, queryset = Like.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'profiles', 'posts', 'comments', 'likes']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['owner', 'Following', 'Followers', 'profile_photo', 'DOB']