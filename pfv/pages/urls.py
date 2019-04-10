from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/', views.photo, name='photo'),
    path('video/', views.video, name='video'),
    path('contact/', views.contact, name='contact')
]
