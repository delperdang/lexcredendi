from import_export import resources 
from piety.models import Record


class RecordResource(resources.ModelResource):

    class Meta:
        model = Record