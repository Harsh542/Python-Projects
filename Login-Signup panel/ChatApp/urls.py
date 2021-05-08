from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   path('login/', views.login, name="login"),
   path('create/', views.create, name="create"),
   path('exist/', views.exist, name="exist"),
   path('home/', views.home, name="home"),
   path('logout/', views.logout, name="logout"),
   path('forgotPassword/', views.forgotPassword, name="forgotPassword"),
   path('enter/', views.enter, name="enter"),
   path('permit/<int:mid>', views.permit, name="permit"),
   path('message/<int:nid>', views.message, name="message"),

]
