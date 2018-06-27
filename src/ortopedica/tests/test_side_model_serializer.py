from django.test import TestCase

from ..serializers import SideModelSerializer


class TestSideModelSerializer(TestCase):
    def setUp(self):
        self.VALID_DATA = {
            "name": "any name",
            "enabled": False
        }
        self.INVALID_DATA = {
        }

    def test_is_valid(self):
        assert SideModelSerializer(data=self.VALID_DATA).is_valid()

    def test_is_invalid(self):
        assert not SideModelSerializer(data=self.INVALID_DATA).is_valid()
