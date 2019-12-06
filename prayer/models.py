from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Record(models.Model):
    code = models.CharField(_('Code'), max_length=255, primary_key=True)
    english_title = models.CharField(_('English Title'), max_length=255)
    english_text = models.CharField(_('English Text'), max_length=4000)
    english_comment = models.CharField(_('English Comment'), max_length=255, blank=True, null=True)
    latin_title = models.CharField(_('Latin Title'), max_length=255, blank=True, null=True)
    latin_text = models.CharField(_('Latin Text'), max_length=4000, blank=True, null=True)
    latin_comment = models.CharField(_('Latin omment'), max_length=255, blank=True, null=True)
    def __str__(self):
        return ('{}').format(self.english_title)
    class Meta:
        verbose_name_plural = "Records"