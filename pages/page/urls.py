from django.urls import path
from .views import *

urlpatterns = [
    path('', post, name="home"),
    path('sermons/', sermons, name="sermons"),
    path('devotions/', devotions, name="devotions"),
    path('devotion/<int:pk>/', post_detail, name='post_detail'),
    path('sermon/<int:pk>/', sermon_detail, name='sermon_detail'),
    path('try/', tryy, name="try"),
    
]
