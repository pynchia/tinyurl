from rest_framework import viewsets
# from rest_framework.reverse import reverse
from short.models import Entry
from . import serializers


class EntryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Entry.objects.all()
    serializer_class = serializers.EntrySerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EntryListSerializer
        else:
            return super(EntryViewSet, self).get_serializer_class()
