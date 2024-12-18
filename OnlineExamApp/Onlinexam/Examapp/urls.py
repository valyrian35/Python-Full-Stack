from django.urls import path

from Examapp import views


urlpatterns = [
    path('starttest/', views.starttest),
    path('nextQuestion/', views.nextQuestion),
    path('prevQuestion/', views.prevQuestion),

]
