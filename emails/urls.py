from django.urls import path
from . import views

urlpatterns = [
   
    path('output',views.output,name='output'),
    path('',views.index,name='index')
    
]