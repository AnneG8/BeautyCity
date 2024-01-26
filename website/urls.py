from django.urls import path, include

from . import views

urlpatterns = [
    # path('login/', views.login_client, name='login'),
    # path('register/', views.register_client, name='register'),
    # path('auth/', include('djoser.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
