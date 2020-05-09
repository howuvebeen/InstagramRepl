from django.shortcuts import render

from rest_framework.views import APIView
from newsfeed.models import Post
from newsfeed.serializers import PostSerializer

from rest_framework.response import Response
from rest_framework import status


class PostList(APIView):
    """
    Retrieve, update or delete a post instance.
    """

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
