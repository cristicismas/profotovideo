from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    slides = models.TextField()

    def __str__(self):
        return self.title

    def album_slides(self):
        return self.slides.split('\n')
    