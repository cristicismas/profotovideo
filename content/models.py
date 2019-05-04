from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    slides = models.TextField()

    def __str__(self):
        return self.title

    def album_slides(self):
        return self.slides.split('\n')


class Photo(models.Model):
    url = models.URLField(max_length=200)
    thumbnail = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=70, blank=True)
    date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Video(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=70, blank=True)
    date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.url
