import uuid

import factory
from faker import Factory
from fe_core.factories import EntityFactory, UserFactory

from ..models import Institution

fake = Factory.create('pt_BR')


class InstitutionFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: str(uuid.uuid4()))
    user = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)
    identifier = fake.building_number()
    contact = fake.name()
    doctor = fake.name()
    address = factory.Sequence(lambda n: str(uuid.uuid4()))

    class Meta:
        model = Institution
