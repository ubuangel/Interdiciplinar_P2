from django.contrib import admin
from django.urls import path

from .import views
urlpatterns = [
  
  
    
    path('', views.home, name='home'),
    path('servicios',views.home,name='servicios'),
    path('tienda',views.home,name='tienda'),
    path('blog',views.tienda,name='blog'),
    path('contacto',views.contacto ,name='contacto'),
    path('calculo',views.calculo,name='calculo'),
]
