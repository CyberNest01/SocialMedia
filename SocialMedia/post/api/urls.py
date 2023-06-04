from django.urls import path, include

urlpatterns = [
    path('', include('post.api.blog.urls')),
    path('category/', include('post.api.category.urls')),
    path('like/', include('post.api.like.urls')),
    path('comments/', include('post.api.comments.urls')),
]
