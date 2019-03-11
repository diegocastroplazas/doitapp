from django.urls import path

"""User's views"""
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.LoginView.as_view() ),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
]