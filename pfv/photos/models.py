from django.db import models

class Photo(models.Model):
    url = models.URLField(max_length=200)
    thumbnail = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=70, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.url
    