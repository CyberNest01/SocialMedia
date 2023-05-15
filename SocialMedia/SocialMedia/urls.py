"""
URL configuration for SocialMedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media",
        default_version='v1',
        description="This api uses for Social Media by NovinParva.com .",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@novinparva.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path('docs/v1/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_refresh'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/admin/token/', jwt_views.TokenObtainPairView.as_view(), name='token_refresh'),
    path('api/admin/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]

urlpatterns += [path('', include('client.urls'))]
urlpatterns += [path('', include('post.urls'))]
urlpatterns += [path('', include('chat.urls'))]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
