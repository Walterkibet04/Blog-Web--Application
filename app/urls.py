from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.Home, name='home'),
    path('base/', views.Base, name='base'),
    path('about/', views.About, name='About'),
    path('singleblog/', views.BlogSingle, name='home'),
    path('contact/', views.Contact, name='home'),
    path('single/', views.Single, name='single'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)