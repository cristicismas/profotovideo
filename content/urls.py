from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo', views.photos, name='photo'),
    path('video', views.videos, name='video'),
    path('albums', views.albums, name='albums'),
    path('admin/shuffle', views.shuffle, name='shuffle'),
    path('admin/content/photo/add_photos', views.add_photos, name='add_photos')
]
