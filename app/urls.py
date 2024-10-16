from django.urls import path
from . import views
from .views import download_pdf, download_excel
from .views import download_page
# Register all urls here
urlpatterns = [
    path('home/', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('login/', views.Login, name = 'login'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('data/', views.data, name = 'data'),
    path('base/', views.base, name = 'base'),
    path('nav/', views.nav, name = 'nav'),
    path('download/pdf/', download_pdf, name='download-pdf'),
    path('download/excel/', download_excel, name='download-excel'),
    path('download/', download_page, name='download-page'),
]