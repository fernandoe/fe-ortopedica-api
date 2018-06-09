from rest_framework import serializers

from .models import Institution


class InstitutionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('uuid', 'created_at', 'updated_at', 'identifier', 'contact', 'doctor', 'address')
