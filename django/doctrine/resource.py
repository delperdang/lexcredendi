from import_export import resources 
from doctrine.models import Record

class RecordResource(resources.ModelResource):

    class Meta:
        model = Record
        exclude = ('id')
        import_id_fields = ['code']
