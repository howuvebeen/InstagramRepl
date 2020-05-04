from django.contrib import admin
from django.urls import path
import user.views

urlpatterns = [
    path('', user.views.AuthView().as_view(), name="authentication")
]
