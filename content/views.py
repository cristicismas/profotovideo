from django.shortcuts import render

from .models import Photo, Album, Video


def index(request):
    photos = Photo.objects.filter(isFeatured=True)
    videos = Video.objects.all()

    context = {
        'photos': photos,
        'videos': videos
    }

    return render(request, 'index.html', context)


def albums(request):
    albums = Album.objects.all()

    context = {
        'albums': albums
    }

    return render(request, 'albums.html', context)


def photos(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos
    }

    return render(request, 'photo.html', context)


def videos(request):
    videos = Video.objects.all()

    context = {
        'videos': videos
    }

    return render(request, 'video.html', context)
