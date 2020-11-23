"""django_my URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from project import views

# 地址配置文件
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index),
    url(r'^', include('pay.urls')),
    # url(r'^', include('project.views'))
    #两种写法都行，配置url访问地址
    url(r'^login$', views.login),
    url(r'^userlogin/$', views.userlogin),
    url(r'^getVerification/$', views.getVerification),
    url(r'^userregister/$', views.userregister),
    url(r'^rechecking/$', views.rechecking),
    url(r'^textrechecking/$', views.textRechecking)
]
