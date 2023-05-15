from django.urls import path, include

urlpatterns = [
    path('', include('client.api.auth.urls'))
]
