from django.urls import path
from loginapp import views

urlpatterns = [
  path('login/', views.login),
  path('register/', views.register) 
  

]