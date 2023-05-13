from django.urls import path, include

app_name = 'client'

urlpatterns = [
    path('accounts/', include(f'{app_name}.views.urls')),
    path(f'api/{app_name}/', include(f'{app_name}.api.urls')),
    path(f'admin/admin/{app_name}/', include(f'{app_name}.admin.urls'))
]
