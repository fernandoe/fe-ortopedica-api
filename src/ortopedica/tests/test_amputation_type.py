from django.test import TestCase

from .factories import AmputationTypeFactory
from ..models import AmputationType


class TestAmputationType(TestCase):

    def test_factory(self):
        assert isinstance(AmputationTypeFactory(), AmputationType)

    def test_name(self):
        assert str(AmputationTypeFactory(name='test_name')) == 'test_name'
