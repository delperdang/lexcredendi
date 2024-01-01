from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bible.resource import RecordResource
from bible.models import Record


class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

admin.site.register(Record, RecordAdmin)
