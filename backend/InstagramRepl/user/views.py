from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ExampleView(APIView):
    def get(self, request):
        content = {'message': 'Hello, world'}
        return Response(content)
