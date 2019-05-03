from django.shortcuts import render

from .models import Photo

def index(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos
    }

    return render(request, 'photo.html', context)
