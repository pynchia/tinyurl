from rest_framework import viewsets
# from rest_framework.reverse import reverse
from short.models import Entry
from . import serializers


class EntryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    The 'list' action allows searching (case ins.) for a substring
    of the long URL via the url param. (e.g. /api/entries/?url=<substring>)
    """
    queryset = Entry.objects.all()
    serializer_class = serializers.EntrySerializer

    def get_queryset(self):
        substring = self.request.query_params.get('url', None)
        if substring is not None:
            return self.queryset.filter(url__contains=substring.lower())
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EntryListSerializer
        return super(EntryViewSet, self).get_serializer_class()
