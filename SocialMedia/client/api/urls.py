from django.urls import path, include

urlpatterns = [
    path('', include('client.api.auth.urls')),
    path('client/', include('client.api.client.urls'))
]
