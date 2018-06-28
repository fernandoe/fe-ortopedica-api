from django.test import TestCase

from .factories import SideFactory
from ..models import Side


class TestSide(TestCase):

    def test_factory(self):
        assert isinstance(SideFactory(), Side)

    def test_name(self):
        assert str(SideFactory(name='test_name')) == 'test_name'
