from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_main, name='main'),
    path('index/', views.get_index, name='index'),
    path('generic/', views.get_generic, name='generic'),
    path('elements/', views.get_elements, name='elements'),
]
