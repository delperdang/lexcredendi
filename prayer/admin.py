from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from prayer.resource import RecordResource
from prayer.models import Record


class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

admin.site.register(Record, RecordAdmin)
