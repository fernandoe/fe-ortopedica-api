from django.test import TestCase

from .factories import ColorFactory
from ..models import Color


class TestColor(TestCase):
    def test_factory(self):
        assert isinstance(ColorFactory(), Color)

    def test_name(self):
        assert str(ColorFactory(name='test_name')) == 'test_name'
