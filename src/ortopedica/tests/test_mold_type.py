from django.test import TestCase

from .factories import MoldTypeFactory
from ..models import MoldType


class TestMoldType(TestCase):
    def test_factory(self):
        assert isinstance(MoldTypeFactory(), MoldType)

    def test_name(self):
        assert str(MoldTypeFactory(name='test_name')) == 'test_name'
