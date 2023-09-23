from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('login/', views.Login, name = 'login'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('data/', views.data, name = 'data'),
    path('base/', views.base, name = 'base'),
    path('nav/', views.nav, name = 'nav'),
]