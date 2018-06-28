from rest_framework.routers import DefaultRouter

from .views import InstitutionModelViewSet, MakingModelViewSet, ColorModelViewSet, SideModelViewSet, \
    AmputeeMemberModelViewSet, AmputationReasonModelViewSet, TechnicalResponsibleModelViewSet, SituationModelViewSet, \
    AmputationTypeModelViewSet, MoldTypeModelViewSet

router = DefaultRouter()
router.register(r'making', MakingModelViewSet, base_name='making')
router.register(r'color', ColorModelViewSet, base_name='color')
router.register(r'side', SideModelViewSet, base_name='side')
router.register(r'amputee-member', AmputeeMemberModelViewSet, base_name='amputee-member')
router.register(r'amputation-reason', AmputationReasonModelViewSet, base_name='amputation-reason')
router.register(r'technical-responsible', TechnicalResponsibleModelViewSet, base_name='technical-responsible')
router.register(r'situation', SituationModelViewSet, base_name='situation')
router.register(r'amputation-type', AmputationTypeModelViewSet, base_name='amputation-type')
router.register(r'mold-type', MoldTypeModelViewSet, base_name='mold-type')
router.register(r'institution', InstitutionModelViewSet, base_name='institution')
urlpatterns = router.urls
