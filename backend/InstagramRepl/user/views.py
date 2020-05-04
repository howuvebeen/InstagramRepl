from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ExampleView(APIView):
    def get(self, request):
        content = {'message': 'Hello, world'}
        return Response(content)


class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        content = {
            # `django.contrib.auth.User` instance.
            'user': unicode(request.user),
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

