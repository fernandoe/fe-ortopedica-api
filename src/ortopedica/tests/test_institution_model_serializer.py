from django.test import TestCase
from ..serializers import InstitutionModelSerializer
import uuid


class TestInstitutionModelSerializer(TestCase):

    def setUp(self):
        self.VALID_DATA = {
            "identifier": "001",
            "contact": "Fulano",
            "doctor": "Ciclano",
            "address": str(uuid.uuid4())
        }
        self.INVALID_DATA = {
            "identifier": "112233445566"
        }

    def test_is_valid(self):
        assert InstitutionModelSerializer(data=self.VALID_DATA).is_valid()

    def test_is_invalid(self):
        assert not InstitutionModelSerializer(data=self.INVALID_DATA).is_valid()
