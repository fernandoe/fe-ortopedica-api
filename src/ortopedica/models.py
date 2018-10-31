from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from fe_core.models import Entity, UUIDModel

User = get_user_model()


class AmputationReason(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class AmputeeMember(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class InstitutionManager(models.Manager):
    def search(self, query=None):
        filters = Q()
        if query:
            filters = filters & Q(name__icontains=query)
            return super(InstitutionManager, self).get_query_set().filter(filters)
        else:
            return super(InstitutionManager, self).get_query_set()


class Institution(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    identifier = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, null=True, blank=True)
    doctor = models.CharField(max_length=50, null=True, blank=True)
    address = models.UUIDField(null=True, blank=True)
    objects = InstitutionManager()

    class Meta:
        ordering = ("name",)


class Situation(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Color(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class AmputationType(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Making(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Side(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class TechnicalResponsible(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class MoldType(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Patient(UUIDModel):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Masculino'),
        (GENDER_FEMALE, 'Feminino')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    transient = models.BooleanField(default=True)
    name = models.CharField(max_length=80, null=True)
    address = models.UUIDField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    phone1 = models.CharField(max_length=15, null=True, blank=True)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    phone3 = models.CharField(max_length=50, null=True, blank=True)
    amputation_reason = models.ForeignKey(AmputationReason, on_delete=models.CASCADE, null=True, blank=True)
    amputee_member = models.ForeignKey(AmputeeMember, on_delete=models.CASCADE, null=True, blank=True)

    address = models.CharField(max_length=80, null=True, blank=True)
    neighborhood = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    profissao = models.CharField(max_length=30, null=True, blank=True)
    altura = models.CharField(max_length=10, null=True, blank=True)
    peso = models.CharField(max_length=10, null=True, blank=True)
    protetizacao = models.CharField(max_length=50, null=True, blank=True)
    tempo_amputacao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
