from rest_framework import serializers
from short.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(source='get_link', read_only=True)

    class Meta:
        model = Entry


class EntryListSerializer(serializers.ModelSerializer):
    entry_url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Entry
        exclude = ('url', 'created_on', 'num_hits')
