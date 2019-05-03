from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'isFeatured', 'url')
  list_display_links = ('id', 'title', 'url')
  list_editable = ('isFeatured',)
  list_filter = ('isFeatured',)

admin.site.register(Video, VideoAdmin)