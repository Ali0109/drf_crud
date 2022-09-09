from rest_framework import serializers

from crud.models import *


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = [
            'id',
            'name',
            'phone',
            'region',
            'country',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
