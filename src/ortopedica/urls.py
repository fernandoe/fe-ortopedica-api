from rest_framework.routers import DefaultRouter

from .views import InstitutionModelViewSet


router = DefaultRouter()
router.register(r'institution', InstitutionModelViewSet, base_name='institution')
urlpatterns = router.urls
