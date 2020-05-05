from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView

# Create your views here.


# class Template_View(TemplateView):

#     template_name = "registration_email.html"
