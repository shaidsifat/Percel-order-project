from django.contrib import admin  
from django.urls import path  
from . import views  
urlpatterns = [  
      
    path('createneworder/', views.createnewpercels),  
    path('createorder/',views.createorders),
    path('checkbox/',views.checkorders),
    path('newpage/',views.new_page)
]  