from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from piety.resource import RecordResource
from piety.models import Record

class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

admin.site.register(Record, RecordAdmin)
