from django.urls import path
from . import views

boosts = views.BoostViewSet.as_view({ 
    'get': 'list', 
    'post': 'create',
})

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('', views.index, name='index'),
    path('login/', views.User_login.as_view(), name='login'),
    path('call_click/', views.call_click),
    path('logout/', views.user_logout, name='logout'),
    path('boosts/', boosts, name='boosts')
]