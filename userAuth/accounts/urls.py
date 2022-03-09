from knox import views as knox_views
from .views import LoginAPI
from django.urls import path, re_path

urlpatterns = [
    re_path('api/login/', LoginAPI.as_view(), name='login'),
    re_path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    re_path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]