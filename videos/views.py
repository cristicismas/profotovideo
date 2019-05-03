from django.shortcuts import render

from .models import Video

def index(request):
    videos = Video.objects.all()

    context = {
        'videos': videos
    }

    return render(request, 'video.html', context)
