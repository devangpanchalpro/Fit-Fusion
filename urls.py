"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import viewsyy
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
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('price/', views.price, name='price'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('elements/', views.elements, name='elements'),
    path('supplement/', views.supplement, name='supplement'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('confirm_password/', views.confirm_password, name='confirm_password'),
    path('shop', views.shop, name='shop'), 
    path('detail/', views.detail, name='detail') ,
    path('checkout/', views.checkout, name='checkout') ,
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart') ,
    path('cart_delete/<int:id>', views.cart_delete, name='cart_delete') ,
    path('cart_plus/<int:id>', views.cart_plus, name='cart_plus') ,
    path('cart_minus/<int:id>', views.cart_minus, name='cart_minus') ,
    
]
