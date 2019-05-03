from django.contrib import admin

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'isFeatured', 'url')
  list_display_links = ('id', 'title', 'url')
  list_editable = ('isFeatured',)
  list_filter = ('isFeatured',)

admin.site.register(Photo, PhotoAdmin)