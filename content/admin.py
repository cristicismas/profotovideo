from django.contrib import admin

from .models import Album, Photo, Video


admin.site.register(Album)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'isFeatured', 'image_name')
    list_display_links = ('id', 'image_name')
    list_editable = ('isFeatured',)
    list_filter = ('isFeatured',)
    readonly_fields = ('preview',)
    list_per_page = 25

    def image_name(self, obj):
        return obj.image.public_id



admin.site.register(Photo, PhotoAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'isFeatured', 'url')
    list_display_links = ('id', 'url')
    list_editable = ('isFeatured',)
    list_filter = ('isFeatured',)
    readonly_fields = ('preview',)


admin.site.register(Video, VideoAdmin)
