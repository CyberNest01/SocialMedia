from django.urls import path, include
from . import *

urlpatterns = [
    path('', ClientLogin.as_view()),
    path('register/', ClientRegister.as_view()),
    path('get_me/', GetMe.as_view()),
    path('edit_profile/', EditProfile.as_view()),
]
