from django.shortcuts import render

from .models import Album

def index(request):
    albums = Album.objects.all()

    context = {
        'albums': albums
    }

    return render(request, 'albums.html', context)
