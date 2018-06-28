from django.test import TestCase

from ..serializers import MakingModelSerializer


class TestMakingModelSerializer(TestCase):
    def setUp(self):
        self.VALID_DATA = {
            "name": "any name",
            "enabled": False
        }
        self.INVALID_DATA = {
        }

    def test_is_valid(self):
        assert MakingModelSerializer(data=self.VALID_DATA).is_valid()

    def test_is_invalid(self):
        assert not MakingModelSerializer(data=self.INVALID_DATA).is_valid()
