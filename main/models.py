from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    full_description = models.TextField()

    def __str__(self):
        return self.title