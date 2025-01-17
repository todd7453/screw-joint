"""
URL configuration for screw_joint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),  # calculator 앱의 URL 포함
    path('home', views.home),
    path('force_analysis', views.force_analysis),
    path('shouli1', views.shouli1),
    path('shouli2', views.shouli2),
    path('shouli3', views.shouli3),
    path('shouli4', views.shouli4),
    path('shouli5', views.shouli5),
    path('shouli6', views.shouli6),
    path('shouli7', views.shouli7),
    path('strength_calculation', views.strength_calculation),
    path('qiangdu1', views.qiangdu1),
    path('qiangdu2', views.qiangdu2),
    path('qiangdu3', views.qiangdu3),
    path('qiangdu4', views.qiangdu4),
    path('qiangdu5', views.qiangdu5),
    path('qiangdu6', views.qiangdu6),
    path('calculator/force_analysis/standard_support/', views.standard_support, name='standard_support'),
    path('calculator/strength_calculation/standard_support/', views.standard_support, name='standard_support')
]