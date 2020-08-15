from rest_framework import serializers
from .models import Temple_Offering


class Temple_Offering_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Temple_Offering
        fields = ['offering_id', 'offering_price']


class TempleOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple_Offering
        fields = [
            'offering_temple_name',
            'offering_id',
            'offering_price',
        ]
