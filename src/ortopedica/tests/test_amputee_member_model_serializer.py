from django.test import TestCase

from ..serializers import AmputeeMemberModelSerializer


class TestAmputeeMemberModelSerializer(TestCase):
    def setUp(self):
        self.VALID_DATA = {
            "name": "any name",
            "enabled": False
        }
        self.INVALID_DATA = {
        }

    def test_is_valid(self):
        assert AmputeeMemberModelSerializer(data=self.VALID_DATA).is_valid()

    def test_is_invalid(self):
        assert not AmputeeMemberModelSerializer(data=self.INVALID_DATA).is_valid()
