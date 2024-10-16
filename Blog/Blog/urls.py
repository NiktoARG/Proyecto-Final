"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import *
from Blog import views

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='home'),
    # path('post/', include('about_us.urls'),),
    path('blog/', blog, name='blog'),
    path('contact/', contacto, name='contact'),
    path('acerca-de/', acerca_de, name='about'),
    path('detalle-posteo/', post, name='post-details'),
    path('log-in/', log_in, name='log-in'),
    path('register/', registrar, name='register'),
    path('recuperar/', recuperar, name='recuperar')
]
