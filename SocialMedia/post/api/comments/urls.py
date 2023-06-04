from django.urls import path, include
from . import *

urlpatterns = [
    path('', CommentSingle.as_view()),
    path('<int:pk>/', CommentSingle.as_view()),
    path('post/<int:pk>/', ListCommentPost.as_view()),
    path('my/list/', MyCommentsList.as_view()),
]
