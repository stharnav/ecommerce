from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/', views.products_page, name='products'),

]
