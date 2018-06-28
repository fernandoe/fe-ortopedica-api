from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from .factories import MoldTypeFactory
from ..models import MoldType

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TestMoldTypeModelViewSet(APITestCase):
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
        response = self.client.post(reverse('mold-type-list'), {
            'name': 'any name',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        obj = MoldType.objects.get(uuid=response.data['uuid'])
        self.assertIsNone(obj.entity)
        self.assertEqual(obj.user, self.user)

    def test_create_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        response = self.client.post(reverse('mold-type-list'), {
            'name': 'any name'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        obj = MoldType.objects.get(uuid=response.data['uuid'])
        self.assertEqual(obj.entity, self.entity)
        self.assertEqual(obj.user, self.user_with_entity)

    def test_get_with_user(self):
        obj = MoldTypeFactory(user=self.user)
        response = self.client.get(reverse('mold-type-detail', kwargs={'pk': str(obj.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entity = response.data
        self.assertTrue('uuid' in entity)
        self.assertTrue('created_at' in entity)
        self.assertTrue('updated_at' in entity)
        self.assertTrue('name' in entity)
        self.assertTrue('enabled' in entity)
        self.assertEqual(5, len(entity))

    def test_get_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        obj = MoldTypeFactory(user=self.user, entity=self.entity)
        response = self.client.get(reverse('mold-type-detail', kwargs={'pk': str(obj.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entity = response.data
        self.assertTrue('uuid' in entity)
        self.assertTrue('created_at' in entity)
        self.assertTrue('updated_at' in entity)
        self.assertTrue('name' in entity)
        self.assertTrue('enabled' in entity)
        self.assertEqual(5, len(entity))

    def test_update_with_user_with_patch(self):
        obj = MoldTypeFactory(user=self.user)
        response = self.client.patch(reverse('mold-type-detail', kwargs={'pk': str(obj.uuid)}), {
            'name': 'ABC'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        obj.refresh_from_db()
        self.assertEqual(obj.name, 'ABC')

    def test_update_with_user_with_put(self):
        obj = MoldTypeFactory(user=self.user)
        response = self.client.put(reverse('mold-type-detail', kwargs={'pk': str(obj.uuid)}), {
            'name': obj.name,
            'enabled': obj.enabled
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        obj.refresh_from_db()
        self.assertEqual(obj.name, response.data['name'])
        self.assertEqual(obj.enabled, response.data['enabled'])

    def test_delete_with_user(self):
        obj = MoldTypeFactory(user=self.user)
        self.assertEqual(1, MoldType.objects.filter(uuid=obj.uuid).count())
        response = self.client.delete(reverse('mold-type-detail', kwargs={'pk': str(obj.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, MoldType.objects.filter(uuid=obj.uuid).count())

