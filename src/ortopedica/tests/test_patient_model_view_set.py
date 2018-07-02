import uuid

from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from .factories import PatientFactory
from ..models import Patient


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TestPatientModelViewSet(APITestCase):
    def setUp(self):
        self.user = UserFactory(entity=None)
        payload = jwt_payload_handler(self.user)
        user_token = jwt_encode_handler(payload)

        self.entity = EntityFactory()
        self.user_with_entity = UserFactory(entity=self.entity)
        payload = jwt_payload_handler(self.user_with_entity)
        self.user_with_entity_token = jwt_encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token)

    def test_create_with_only_user(self):
        response = self.client.post(reverse('patient-list'), {
            'identifier': '123',
            'contact': 'Fulano',
            'doctor': 'Ciclano',
            'address': str(uuid.uuid4()),
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        institution = Patient.objects.get(uuid=response.data['uuid'])
        self.assertIsNone(institution.entity)
        self.assertEqual(institution.user, self.user)

    def test_create_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        response = self.client.post(reverse('patient-list'), {
            'identifier': '123',
            'contact': 'Fulano',
            'doctor': 'Ciclano',
            'address': str(uuid.uuid4()),
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        institution = Patient.objects.get(uuid=response.data['uuid'])
        self.assertEqual(institution.entity, self.entity)
        self.assertEqual(institution.user, self.user_with_entity)

    def test_get_with_user(self):
        institution = PatientFactory(user=self.user)
        response = self.client.get(reverse('patient-detail', kwargs={'pk': str(institution.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entity = response.data
        self.assertTrue('uuid' in entity)
        self.assertTrue('created_at' in entity)
        self.assertTrue('updated_at' in entity)
        self.assertTrue('name' in entity)
        self.assertTrue('city' in entity)
        self.assertTrue('phone1' in entity)
        self.assertTrue('phone2' in entity)
        self.assertTrue('phone3' in entity)
        self.assertEqual(8, len(entity))

    def test_get_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        institution = PatientFactory(user=self.user, entity=self.entity)
        response = self.client.get(reverse('patient-detail', kwargs={'pk': str(institution.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entity = response.data
        print(entity)
        self.assertTrue('uuid' in entity)
        self.assertTrue('created_at' in entity)
        self.assertTrue('updated_at' in entity)
        self.assertTrue('name' in entity)
        self.assertTrue('city' in entity)
        self.assertTrue('phone1' in entity)
        self.assertTrue('phone2' in entity)
        self.assertTrue('phone3' in entity)
        self.assertEqual(8, len(entity))

    def test_update_with_user_with_patch(self):
        institution = PatientFactory(user=self.user)
        response = self.client.patch(reverse('patient-detail', kwargs={'pk': str(institution.uuid)}), {
            'name': 'ABC'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        institution.refresh_from_db()
        self.assertEqual(institution.name, 'ABC')

    def test_update_with_user_with_put(self):
        institution = PatientFactory(user=self.user)
        response = self.client.put(reverse('patient-detail', kwargs={'pk': str(institution.uuid)}), {
            'name': institution.name,
            'city': institution.city,
            'phone1': institution.phone1,
            'phone2': institution.phone2,
            'phone3': institution.phone3
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        institution.refresh_from_db()
        self.assertEqual(institution.name, response.data['name'])
        self.assertEqual(institution.city, response.data['city'])
        self.assertEqual(institution.phone1, response.data['phone1'])
        self.assertEqual(institution.phone2, response.data['phone2'])
        self.assertEqual(institution.phone3, response.data['phone3'])

    def test_delete_with_user(self):
        institution = PatientFactory(user=self.user)
        self.assertEqual(1, Patient.objects.filter(uuid=institution.uuid).count())
        response = self.client.delete(reverse('patient-detail', kwargs={'pk': str(institution.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, Patient.objects.filter(uuid=institution.uuid).count())
