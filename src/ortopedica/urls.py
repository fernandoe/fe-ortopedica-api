from django.urls import path

from .views import InstitutionModelViewSet


urlpatterns = [
    path('institution', InstitutionModelViewSet.as_view(), name='Institution')
]
