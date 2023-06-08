from django.urls import path, include

urlpatterns = [
    path('', include('story.api.story.urls')),
]
