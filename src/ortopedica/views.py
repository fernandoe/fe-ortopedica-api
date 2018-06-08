from rest_framework import viewsets

from .models import Institution
from .serializers import InstitutionModelSerializer


class InstitutionModelViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionModelSerializer
