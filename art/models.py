from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Record(models.Model):
    filename = models.CharField(_('Filename'), max_length=255, primary_key=True)
    title = models.CharField(_('Title'), max_length=255)
    album = models.CharField(_('Album'), max_length=255)
    artist = models.CharField(_('Artist'), max_length=255, blank=True, null=True)
    rough_date = models.CharField(_('Rough Date'), max_length=255, blank=True, null=True)
    def __str__(self):
        return ('{}').format(self.title)
    class Meta:
        verbose_name_plural = "Records"
