from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

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


@staff_member_required
def shuffle(request):
    request_origin = request.META['HTTP_REFERER']

    if 'photo' in request_origin:
        objects = Photo.objects.all().order_by('?')

    elif 'video' in request_origin:
        objects = Video.objects.all().order_by('?')

    else:
        objects = Album.objects.all().order_by('?')

    for current_object in objects:
        current_object.save()

    return HttpResponseRedirect(request_origin)
