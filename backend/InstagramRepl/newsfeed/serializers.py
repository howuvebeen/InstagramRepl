from rest_framework import serializers

from newsfeed.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['owner', 'photo', 'description']
