from django.db import models

class Video(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=70, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    