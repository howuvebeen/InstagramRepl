from django.urls import path, include, re_path
import user.views

urlpatterns = [
    path('', include('rest_registration.api.urls')),
]
