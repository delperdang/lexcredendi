from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from art.resource import RecordResource
from art.models import Record

class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

# Register your models here.

admin.site.register(Record, RecordAdmin)
