from django.test import TestCase

from .factories import MakingFactory
from ..models import Making


class TestMaking(TestCase):

    def test_factory(self):
        assert isinstance(MakingFactory(), Making)

    def test_name(self):
        assert str(MakingFactory(name='test_name')) == 'test_name'
