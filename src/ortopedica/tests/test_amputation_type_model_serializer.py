from django.test import TestCase

from ..serializers import AmputationTypeModelSerializer


class TestAmputationTypeModelSerializer(TestCase):
    def setUp(self):
        self.VALID_DATA = {
            "name": "any name",
            "enabled": False
        }
        self.INVALID_DATA = {
        }

    def test_is_valid(self):
        assert AmputationTypeModelSerializer(data=self.VALID_DATA).is_valid()

    def test_is_invalid(self):
        assert not AmputationTypeModelSerializer(data=self.INVALID_DATA).is_valid()
