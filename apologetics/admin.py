from django.contrib import admin
from apologetics.models import Record
from import_export import resources

# Register your models here.

admin.site.register(Record)

class RecordResource(resources.ModelResource):

    class Meta:
        model = Record
