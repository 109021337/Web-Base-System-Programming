"""chalogin URL Configuration

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
from django.conf.urls import include
from chaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('register/', views.register),
    path('news/', views.news),
    path('question/', views.question),
    path('login/', views.login),
    path('manage/', views.manage),
    path('logout/', views.logout),
    path('aboutus/', views.aboutus),
    path('service/', views.service),
    path('createsucces/', views.createsucces),
    path('captcha/', include('captcha.urls')),
    path('edit/<str:name>/<str:mode>', views.edit),
    path('book/<str:isbn>', views.bookview),
    path('addtocart/<str:ctype>/', views.addtocart),
    path('addtocart/<str:ctype>/<int:bookid>/', views.addtocart),
    path('cart/', views.cart),
    path('cartorder/', views.cartorder),
    path('cartok/', views.cartok),
    path('cartordercheck/', views.cartordercheck),
    # 文學小說
    path('literature1/', views.literature1),
    path('literature2/', views.literature2),
    path('literature3/', views.literature3),
    # 財經企管 
    path('finance1/', views.finance1),
    path('finance2/', views.finance2),
    path('finance3/', views.finance3),
    # 語言
    path('language1/', views.language1),
    path('language2/', views.language2),
    path('language3/', views.language3),
    # 飲食料理 
    path('cooking1/', views.cooking1),
    path('cooking2/', views.cooking2),
    path('cooking3/', views.cooking3),
    # 日本輕小說 
    path('light_novel1/', views.light_novel1),
    path('light_novel2/', views.light_novel2),
    path('light_novel3/', views.light_novel3),
    path('light_novel4/', views.light_novel4),
    # 電腦資訊 
    path('computer1/', views.computer1),
    path('computer2/', views.computer2),
    path('computer3/', views.computer3),
    path('computer4/', views.computer4),
    path('computer5/', views.computer5),
]
