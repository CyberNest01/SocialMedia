from django.urls import path
from . import *


urlpatterns = [
    path('my/list/', MyPostList.as_view()),
    path('friends/list/', FriendsPostList.as_view()),
    path('list/', PostList.as_view()),
    path('list/<int:pk>/', UserPostList.as_view()),

    path('<int:pk>/', PostSingle.as_view()),
    path('', PostSingle.as_view()),
]
