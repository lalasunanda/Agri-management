from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('index/',views.index,name='index'),
   
    path('index3/',views.index3,name='index3'),
   
   
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('index/result/', views.result, name='result'),
   
    path('index3/result3/', views.result3, name='result3'),
    
]