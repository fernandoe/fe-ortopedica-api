from django.test import TestCase

from .factories import SituationFactory
from ..models import Situation


class TestSituation(TestCase):

    def test_factory(self):
        assert isinstance(SituationFactory(), Situation)

    def test_name(self):
        assert str(SituationFactory(name='test_name')) == 'test_name'
