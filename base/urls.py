from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('index', views.index, name='index'),
   
    path('index3', views.index3, name='index3'),
    
  
    path('signup/',views.SignupPage,name='signup'),
    path('result', views.result, name='result'),
    path('result2', views.result2, name='result2'),
    path('result3', views.result3, name='result3'),
    
    
]