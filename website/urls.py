from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('confirm_phone/', views.confirm_phone, name='confirm_phone'),
    path('profile/<int:user_id>/', views.view_profile, name='profile'),

    path('', views.main_page, name="index"),
    path('service/', views.service, name='service'),
    path('popup-login/',views.popup_login_page, name='popup-login'),
    path('popup-tip/', views.popup_tip_page, name='popup-tip'),

    # path('base', views.base_page, name='base'),

    path('api-auth/', include('rest_framework.urls')),
]
