from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('confirm_phone/', views.confirm_phone, name='confirm_phone'),
    path('profile/<int:user_id>/', views.view_profile, name='profile'),
    # path('auth/', include('djoser.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
