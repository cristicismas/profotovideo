from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo', views.photos, name='photo'),
    path('video', views.videos, name='video'),
    path('albums', views.albums, name='albums')
]
