from rest_framework import serializers

from .models import Making, Color, Side, AmputeeMember, Institution


class MakingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Making
        fields = ('uuid', 'created_at', 'updated_at', 'name', 'enabled')


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('uuid', 'created_at', 'updated_at', 'name', 'enabled')


class SideModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Side
        fields = ('uuid', 'created_at', 'updated_at', 'name', 'enabled')


class AmputeeMemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmputeeMember
        fields = ('uuid', 'created_at', 'updated_at', 'name', 'enabled')


class InstitutionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('uuid', 'created_at', 'updated_at', 'identifier', 'contact', 'doctor', 'address')
