from django.urls import path
from . import *


urlpatterns = [
    path('reports/', Reports.as_view()),
    path('request_friends/', RequestFriends.as_view()),
    path('request_friends/<int:pk>/', RequestFriends.as_view()),
    path('request/list/', RequestsList.as_view()),
    path('get/requests/', GetRequests.as_view()),
    path('get/requests/<int:pk>/', GetRequests.as_view()),
    path('remove/request/<int:pk>/', RemoveRequest.as_view()),
    path('friends/list/', FriendsList.as_view()),
]
