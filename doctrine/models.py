from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Record(models.Model):
    code = models.CharField(_('Code'), max_length=255, primary_key=True)
    title = models.CharField(_('Title'), max_length=255)
    text = models.CharField(_('Text'), max_length=4000)
    comment = models.CharField(_('Comment'), max_length=255, blank=True, null=True)
    def __str__(self):
        return ('{}').format(self.title)
    class Meta:
        verbose_name_plural = "Records"
