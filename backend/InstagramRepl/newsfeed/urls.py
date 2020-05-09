from django.urls import path, include, re_path
import newsfeed.views
urlpatterns = [
    path('posts/', newsfeed.views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>', newsfeed.views.PostList.as_view(), name='post'),
]
