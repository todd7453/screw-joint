from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('force_analysis/', views.force_analysis, name='force_analysis'), #受力分析
    path('shouli1/', views.shouli1, name='shouli1'),
    path('shouli2/', views.shouli2, name='shouli2'),
    path('shouli3/', views.shouli3, name='shouli3'),
    path('shouli4/', views.shouli4, name='shouli4'),
    path('shouli5/', views.shouli5, name='shouli5'),
    path('shouli6/', views.shouli6, name='shouli6'),
    path('calculator/force_analysis/standard_support/', views.standard_support, name='standard_support'),
    path('shouli7/', views.shouli7, name='shouli7'),
    path('strength_calculation/', views.strength_calculation, name='strength_calculation'), 
    path('qiangdu1/', views.qiangdu1, name='qiangdu1'),
    path('qiangdu2/', views.qiangdu2, name='qiangdu2'),
    path('qiangdu3/', views.qiangdu3, name='qiangdu3'),
    path('qiangdu4/', views.qiangdu4, name='qiangdu4'),
    path('qiangdu5/', views.qiangdu5, name='qiangdu5'),
    path('qiangdu6/', views.qiangdu6, name='qiangdu6'),
    path('calculator/strength_calculation/standard_support/', views.standard_support, name='standard_support'),
    path('shape_material_analysis/', views.shape_material_analysis, name='shape_material_analysis'),
    path('standard_support/', views.standard_support, name='standard_support'), 
    path('thread_parameter_definition/', views.thread_parameter_definition, name='thread_parameter_definition'), 
]