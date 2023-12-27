from import_export import resources 
from art.models import Record

class RecordResource(resources.ModelResource):

    class Meta:
        model = Record
