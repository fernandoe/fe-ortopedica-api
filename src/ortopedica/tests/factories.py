import uuid

import factory
from faker import Factory
from fe_core.factories import EntityFactory, UserFactory

from ..models import Making, Color, Side, AmputeeMember, Institution

fake = Factory.create('pt_BR')


class MakingFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: str(uuid.uuid4()))
    user = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)
    name = fake.company()

    class Meta:
        model = Making


class ColorFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: str(uuid.uuid4()))
    user = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)
    name = fake.color_name()

    class Meta:
        model = Color


class SideFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: str(uuid.uuid4()))
    user = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)
    name = fake.name()

    class Meta:
        model = Side


class AmputeeMemberFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: str(uuid.uuid4()))
    user = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)
    name = fake.name()

    class Meta:
        model = AmputeeMember


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
