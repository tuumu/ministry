from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('devotions/', views.devotion, name="devotions"),
    path('sermons/', views.sermon, name="sermons"),
    path('devotion/<int:pk>/', views.devotion_detail, name='devotion_detail'),
    path('sermon/<int:pk>/', views.sermon_detail, name='sermon_detail'),
    

]
