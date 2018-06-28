from django.contrib import admin

from .models import Color, Institution, Making, MoldType, AmputationType, Situation, TechnicalResponsible, \
    AmputationReason, AmputeeMember, Side


@admin.register(Making)
class MakingModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(Side)
class SideModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(AmputeeMember)
class AmputeeMemberModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(AmputationReason)
class AmputationReasonModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(TechnicalResponsible)
class TechnicalResponsibleModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(Situation)
class SituationModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(AmputationType)
class AmputationTypeModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(MoldType)
class MoldTypeModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'name')
    list_display = ('get_uuid', 'entity', 'user', 'name', 'enabled')
    ordering = ('name',)


@admin.register(Institution)
class InstitutionModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'identifier', 'contact', 'doctor')
    list_display = ('get_uuid', 'entity', 'user', 'identifier', 'contact', 'doctor', 'address')
    ordering = ('created_at',)
