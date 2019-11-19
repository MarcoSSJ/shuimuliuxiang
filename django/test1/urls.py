"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
import TestModel
from TestModel import urls


urlpatterns = [
    path('admin', admin.site.urls),
    url('^', include(TestModel.urls)),
    #path('logon-form', views.logon_form),
    #path('logon', views.logon),
    #path('login-form', views.login_form),
    #path('login', views.login),
    #path('logout', views.logout),

]
