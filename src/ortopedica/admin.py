from django.contrib import admin

from .models import Institution


@admin.register(Institution)
class InstitutionModelAdmin(admin.ModelAdmin):
    search_fields = ('uuid', 'identifier', 'contact', 'doctor')
    list_display = ('get_uuid', 'entity', 'user', 'identifier', 'contact', 'doctor', 'address')
    ordering = ('created_at',)
