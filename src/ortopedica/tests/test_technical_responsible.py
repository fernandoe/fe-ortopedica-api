from django.test import TestCase

from .factories import TechnicalResponsibleFactory
from ..models import TechnicalResponsible


class TestTechnicalResponsible(TestCase):

    def test_factory(self):
        assert isinstance(TechnicalResponsibleFactory(), TechnicalResponsible)

    def test_name(self):
        assert str(TechnicalResponsibleFactory(name='test_name')) == 'test_name'
