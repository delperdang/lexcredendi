from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apologetics.resource import RecordResource
from apologetics.models import Record

class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

# Register your models here.

admin.site.register(Record, RecordAdmin)
