"""djsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^index', views.index),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    #re_path(r'^cart', views.cart),
    re_path(r'^feedback', views.feedback),
    re_path(r'^valid', views.valid),
    path('admin/', admin.site.urls),
    path('create_comment/', views.create_comment),
    path('get_comment/', views.get_comment)
]
