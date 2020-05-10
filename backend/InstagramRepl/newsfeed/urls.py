from django.urls import path, include, re_path
from newsfeed import views
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post'),
    path('comments/', views.CommentList.as_view(), name = 'comments'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name= 'comment'),
    path('likes/', views.LikeList.as_view(), name= 'likes'),
    path('likes/<int:pk>', views.LikeDetail.as_view(), name= 'like'),
]
