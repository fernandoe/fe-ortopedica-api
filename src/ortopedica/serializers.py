from rest_framework import serializers

from .models import Institution


class InstitutionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('identifier', 'contact', 'doctor', 'address')
