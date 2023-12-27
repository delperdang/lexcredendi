from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from doctrine.resource import RecordResource
from doctrine.models import Record

class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

# Register your models here.

admin.site.register(Record, RecordAdmin)
