"""mysite_w1 URL Configuration
# 路由系统
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import re_path
from django.urls import path
from app01 import views
# from manager import views

from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index ),
    # re_path('login/(\d+)/', views.login),
    # re_path('login2/(?P<p1>\d+)/(?P<x1>\d+)/', views.login2),
    path('web/',include('app01.urls')),
    path('template',views.template)
]
