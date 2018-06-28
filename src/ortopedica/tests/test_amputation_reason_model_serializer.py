from django.test import TestCase

from ..serializers import AmputationReasonModelSerializer


class TestAmputationReasonModelSerializer(TestCase):
    def setUp(self):
        self.VALID_DATA = {
            "name": "any name",
            "enabled": False
        }
        self.INVALID_DATA = {
        }

    def test_is_valid(self):
        assert AmputationReasonModelSerializer(data=self.VALID_DATA).is_valid()

    def test_is_invalid(self):
        assert not AmputationReasonModelSerializer(data=self.INVALID_DATA).is_valid()
