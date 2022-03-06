"""insta URL Configuration

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
from django.urls import re_path as url,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin



urlpatterns = [

    url(r'^$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    # url('',views.home,name = 'home'),
    url('home/', views.home, name='home'),
    url('search/', views.search_results,name='search_results'),
    url('comments/', views.comments,name='comments'),
    url('like/',views.like_post, name='like_post'),
    url('accounts/profile/', views.home,name='profilee'),
    
    
]


