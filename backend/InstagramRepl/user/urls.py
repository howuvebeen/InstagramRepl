from django.contrib import admin
from django.urls import path
import user.views

urlpatterns = [
    path('', user.views.LoginView().as_view(), name="authentication")
]
