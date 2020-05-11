from django.urls import path, include, re_path
from newsfeed import views
urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('comments/', views.CommentList.as_view(), name = 'comment-list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name= 'comment-detail'),
    path('likes/', views.LikeList.as_view(), name= 'like-list'),
    path('likes/<int:pk>', views.LikeDetail.as_view(), name= 'like-detail'),
]
