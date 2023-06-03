from django.urls import path, include
from . import *

urlpatterns = [
    path('', LikePost.as_view()),
    path('<int:pk>/', LikePost.as_view()),
]
