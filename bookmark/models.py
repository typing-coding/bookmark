from django.db import models

# Create your models here.
class Bookmark(models.Model):
    bookmark_name = models.CharField(max_length=100)
    bookmark_url = models.URLField('Site URL')

    def __str__(self):
        return self.bookmark_name