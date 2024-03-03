from django.db import models
from django.utils.translation import gettext as _

class Record(models.Model):
    title = models.CharField(_('Title'), max_length=255, primary_key=True)
    album = models.CharField(_('Album'), max_length=255)
    image = models.ImageField(_('Image'), upload_to="art/img", max_length=100)
    def __str__(self):
        return ('{}').format(self.title)
    class Meta:
        verbose_name_plural = "Records"
