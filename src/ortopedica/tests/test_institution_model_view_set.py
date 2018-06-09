import uuid

from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from .factories import InstitutionFactory
from ..models import Institution


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TestInstitutionModelViewSet(APITestCase):
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
        response = self.client.post(reverse('institution-list'), {
            'identifier': '123',
            'contact': 'Fulano',
            'doctor': 'Ciclano',
            'address': str(uuid.uuid4()),
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        institution = Institution.objects.get(uuid=response.data['uuid'])
        self.assertIsNone(institution.entity)
        self.assertEqual(institution.user, self.user)

    def test_create_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        response = self.client.post(reverse('institution-list'), {
            'identifier': '123',
            'contact': 'Fulano',
            'doctor': 'Ciclano',
            'address': str(uuid.uuid4()),
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        institution = Institution.objects.get(uuid=response.data['uuid'])
        self.assertEqual(institution.entity, self.entity)
        self.assertEqual(institution.user, self.user_with_entity)

    def test_get_with_user(self):
        institution = InstitutionFactory(user=self.user)
        response = self.client.get(reverse('institution-detail', kwargs={'pk': str(institution.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entity = response.data
        self.assertTrue('uuid' in entity)
        self.assertTrue('created_at' in entity)
        self.assertTrue('updated_at' in entity)
        self.assertTrue('identifier' in entity)
        self.assertTrue('contact' in entity)
        self.assertTrue('doctor' in entity)
        self.assertTrue('address' in entity)
        self.assertEqual(7, len(entity))

    def test_get_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        institution = InstitutionFactory(user=self.user, entity=self.entity)
        response = self.client.get(reverse('institution-detail', kwargs={'pk': str(institution.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entity = response.data
        self.assertTrue('uuid' in entity)
        self.assertTrue('created_at' in entity)
        self.assertTrue('updated_at' in entity)
        self.assertTrue('identifier' in entity)
        self.assertTrue('contact' in entity)
        self.assertTrue('doctor' in entity)
        self.assertTrue('address' in entity)
        self.assertEqual(7, len(entity))

    def test_update_with_user_with_patch(self):
        institution = InstitutionFactory(user=self.user)
        response = self.client.patch(reverse('institution-detail', kwargs={'pk': str(institution.uuid)}), {
            'contact': 'ABC'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        institution.refresh_from_db()
        self.assertEqual(institution.contact, 'ABC')

    def test_update_with_user_with_put(self):
        institution = InstitutionFactory(user=self.user)
        response = self.client.put(reverse('institution-detail', kwargs={'pk': str(institution.uuid)}), {
            'identifier': institution.identifier,
            'contact': institution.contact,
            'doctor': institution.doctor,
            'address': institution.address
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        institution.refresh_from_db()
        self.assertEqual(institution.identifier, response.data['identifier'])
        self.assertEqual(institution.contact, response.data['contact'])
        self.assertEqual(institution.doctor, response.data['doctor'])
        self.assertEqual(str(institution.address), response.data['address'])

    def test_delete_with_user(self):
        institution = InstitutionFactory(user=self.user)
        self.assertEqual(1, Institution.objects.filter(uuid=institution.uuid).count())
        response = self.client.delete(reverse('institution-detail', kwargs={'pk': str(institution.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, Institution.objects.filter(uuid=institution.uuid).count())
