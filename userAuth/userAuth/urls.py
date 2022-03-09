"""userAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from knox import views as knox_views
from accounts.views import LoginAPI
from accounts.views import ChangePasswordView
from django.contrib import admin
from django.urls import path, re_path, include
from .views import RegisterAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/register/', RegisterAPI.as_view(), name='register'),
    re_path('api/login/', LoginAPI.as_view(), name='login'),
    re_path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    re_path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    re_path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
] 
