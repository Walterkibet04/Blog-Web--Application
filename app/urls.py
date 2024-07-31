from django.urls import path
from .import views

urlpatterns = [
     path('', views.Home, name='home'),
    path('base/', views.Base, name='About'),
    path('about/', views.About, name='About'),
    path('category/', views.Category, name='category'),
    path('singleblog/', views.BlogSingle, name='home'),
    path('classic/', views.Classic, name='home'),
    path('contact/', views.Contact, name='home'),
    path('minimal/', views.Minimal, name='home'),
    path('personal/', views.Personal, name='home'),
    path('person/', views.PersonalAlt, name='home'),
    path('single/', views.Single, name='home'),
]