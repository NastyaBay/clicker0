from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('', views.index, name='index'),
    path('login/', views.User_login.as_view(), name='login')
]