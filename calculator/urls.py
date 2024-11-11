from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('force_analysis/', views.force_analysis, name='force_analysis'), #受力分析
    path('shouli1/', views.shouli1, name='shouli1'),
    path('shouli2/', views.shouli2, name='shouli2'),
    path('strength_calculation/', views.strength_calculation, name='strength_calculation'), 
    path('shape_material_analysis/', views.shape_material_analysis, name='shape_material_analysis'),
    path('standard_support/', views.standard_support, name='standard_support'), 
    path('thread_parameter_definition/', views.thread_parameter_definition, name='thread_parameter_definition'), 
]