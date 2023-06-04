"""core URL Configuration

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
from products.views import home_view, about_view 
from blogs.views import list_view, create_view, update_view, delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('about/', about_view, name='about'),
    path('list_view/', list_view , name='list_view'),
    path('create/', create_view, name='create'),
    path('update/<id>/', update_view, name='update'),
    path('delete/<id>/', delete_view, name='delete'),
]
