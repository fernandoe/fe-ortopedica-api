from rest_framework import viewsets

from .models import Making, Institution, Color, Side, AmputeeMember, AmputationReason, TechnicalResponsible, Situation, \
    AmputationType, MoldType
from .serializers import MakingModelSerializer, InstitutionModelSerializer, ColorModelSerializer, SideModelSerializer, \
    AmputeeMemberModelSerializer, AmputationReasonModelSerializer, TechnicalResponsibleModelSerializer, \
    SituationModelSerializer, AmputationTypeModelSerializer, MoldTypeModelSerializer


class MakingModelViewSet(viewsets.ModelViewSet):
    queryset = Making.objects.all()
    serializer_class = MakingModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class ColorModelViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class SideModelViewSet(viewsets.ModelViewSet):
    queryset = Side.objects.all()
    serializer_class = SideModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class AmputeeMemberModelViewSet(viewsets.ModelViewSet):
    queryset = AmputeeMember.objects.all()
    serializer_class = AmputeeMemberModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class AmputationReasonModelViewSet(viewsets.ModelViewSet):
    queryset = AmputationReason.objects.all()
    serializer_class = AmputationReasonModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class TechnicalResponsibleModelViewSet(viewsets.ModelViewSet):
    queryset = TechnicalResponsible.objects.all()
    serializer_class = TechnicalResponsibleModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class SituationModelViewSet(viewsets.ModelViewSet):
    queryset = Situation.objects.all()
    serializer_class = SituationModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class AmputationTypeModelViewSet(viewsets.ModelViewSet):
    queryset = AmputationType.objects.all()
    serializer_class = AmputationTypeModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class MoldTypeModelViewSet(viewsets.ModelViewSet):
    queryset = MoldType.objects.all()
    serializer_class = MoldTypeModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)


class InstitutionModelViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, entity=self.request.user.entity)
