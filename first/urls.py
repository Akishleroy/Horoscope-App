"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from horoscope import views

urlpatterns = [
    path('',views.index,name='base-name'),
    path('<int:month>/<int:day>',views.get_sign),
    path('<str:znak_zodiaka>',views.get_info_znak_zodiaka,name='horoscope-name'),
    path('type',views.get_info_style,name='styles-name'),
    path('type/fire',views.get_style_fire),
    path('type/earth',views.get_style_earth),
    path('type/air',views.get_style_air),
    path('type/water',views.get_style_water),
    path('<int:znak_zodiaka>',views.get_info_znak_number),
]
