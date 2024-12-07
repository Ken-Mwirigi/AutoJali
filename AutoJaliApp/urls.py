"""
URL configuration for AutoJali project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from AutoJaliApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('register-type/', views.register_type, name='register-type'),
    path('register-owner/', views.register_owner, name='register-owner'),
    path('register-driver/', views.register_driver, name='register-driver'),

    path('login/', views.car_owner_login, name='login'),
    path('login-driver/', views.driver_login, name='login-driver'),
    path('owner-dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('driver-dashboard/', views.driver_dashboard, name='driver-dashboard'),
    path('after_driver_login/', views.after_driver_login, name='after_driver_login'),
    path('payment/', views.payment, name='payment'),

    path('edit/<int:id>/', views.edit_order, name='edit_order'),
    path('delete/<int:id>/', views.delete_order, name='delete_order'),

    path('confirm_delete/', views.confirm_delete, name='confirm_delete'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('view_driver_details/', views.view_driver_details, name='view_driver_details'),





]
