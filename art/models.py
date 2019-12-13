from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Record(models.Model):
    code = models.CharField(_('Code'), max_length=255, primary_key=True)
    title = models.CharField(_('Title'), max_length=255)
    album = models.CharField(_('Collection'), max_length=255)
    img = models.ImageField(_('Artwork'), default="img.jpg")
    artist = models.CharField(_('Artist'), max_length=255, blank=True, null=True)
    rough_date = models.CharField(_('Date'), max_length=255, blank=True, null=True)
    def __str__(self):
        return ('{}').format(self.title)
    class Meta:
        verbose_name_plural = "Records"
