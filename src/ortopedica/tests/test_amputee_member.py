from django.test import TestCase

from .factories import AmputeeMemberFactory
from ..models import AmputeeMember


class TestAmputeeMember(TestCase):

    def test_factory(self):
        assert isinstance(AmputeeMemberFactory(), AmputeeMember)

    def test_name(self):
        assert str(AmputeeMemberFactory(name='test_name')) == 'test_name'
