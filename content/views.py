from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin, messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .forms import MultiplePhotosForm
from .models import Photo, Album, Video


def index(request):
    photos = Photo.objects.filter(isFeatured=True)

    try:
        video = Video.objects.get(isFeatured=True)
    except:
        video = None

    context = {
        'photos': photos,
        'video': video
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


# Add this to get site meta for the add_photos context
class MyAdminSite(admin.AdminSite):
    pass


@staff_member_required
def add_photos(request):
    form = MultiplePhotosForm()
    mysite = MyAdminSite()

    context = {
        'form': form,
        'opts': Photo._meta,
        'user': request.user,
        'site_header': mysite.site_header,
        'has_permission': mysite.has_permission(request),
        'site_url': mysite.site_url,
        'change': False,
        'add': False,
        'is_popup': False,
        'save_as': True,
        'has_delete_permission': True,
        'has_add_permission': True,
        'has_change_permission': True,
        'has_view_permission': False,
        'has_editable_inline_admin_formsets': True
    }

    if request.method == 'POST':
        form = MultiplePhotosForm(request.POST, request.FILES)
        
        photos = request.FILES.getlist('photos')

        if form.is_valid():
            for photo in photos:
                Photo.objects.create(image=photo)
                HttpResponse('Buffering...')

            messages.success(request, 'Photos added successfully.')
            return HttpResponseRedirect('/admin/content/photo')

        # Add the validated form to context to get validation errors
        context['form'] = form

        return render(request, 'admin/multiple_photos_form.html', context)
    else:
        return render(request, 'admin/multiple_photos_form.html', context)
