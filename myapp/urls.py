from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index.html'),
    path('exercise', views.exercises,name='exercise.html'),
    path('login', views.loginpage,name='login.html'),
    path('register', views.register,name='register.html'),
    path('viewdata', views.viewdata, name='viewdata'),
    path('checkuser', views.checklogin, name='checkuser'),
    path('logout', views.logout, name='logout'),

]