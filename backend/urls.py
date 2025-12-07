from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/', views.products_page, name='products'),
    path('dashboard/',views.dashboard_page,name='dashboard'),
    path('order/',views.order_page,name='orders'),
    path('users/',views.user_page,name='users'),
    path('settings/',views.settings_page,name='settings'),
    path('settings/edit-profile/', views.edit_profile, name='edit_profile'),
    path('settings/change-password/', views.change_password, name='change_password'),
    path("settings/notifications/", views.notification_settings, name="notification_settings"),
    path("settings/privacy/", views.privacy_settings, name="privacy_settings"),
    path("settings/system/", views.system_preferences, name="system_preferences"),
]
