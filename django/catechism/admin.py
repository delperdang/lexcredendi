from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from catechism.resource import RecordResource
from catechism.models import Record

class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource

admin.site.register(Record, RecordAdmin)
