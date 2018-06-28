from django.test import TestCase

from .factories import AmputationReasonFactory
from ..models import AmputationReason


class TestAmputationReason(TestCase):

    def test_factory(self):
        assert isinstance(AmputationReasonFactory(), AmputationReason)

    def test_name(self):
        assert str(AmputationReasonFactory(name='test_name')) == 'test_name'
