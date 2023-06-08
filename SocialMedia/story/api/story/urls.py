from django.urls import path, include
from . import *

urlpatterns = [
    path('', StorySingle.as_view()),
    path('<int:pk>/', StorySingle.as_view()),
    path('my/list/', MyStoryList.as_view()),
    path('friends/list/', FriendsStoryList.as_view()),
]
