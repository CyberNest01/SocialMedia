from django.urls import path
from . import *


urlpatterns = [
    path('reports/', Reports.as_view()),
]
