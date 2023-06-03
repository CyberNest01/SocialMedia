from django.urls import path
from . import *


urlpatterns = [
    path('list/', CategoryList.as_view()),
    path('', CategorySingle.as_view()),
    path('<int:pk>/', CategorySingle.as_view()),
]
