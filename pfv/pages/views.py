from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def photo(request):
    return render(request, 'pages/photo.html')


def video(request):
    return render(request, 'pages/video.html')


def contact(request):
    return render(request, 'pages/contact.html')
