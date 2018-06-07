from django.contrib.auth import get_user_model
from django.db import models
from fe_core.models import Entity

User = get_user_model()


class Institution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    identifier = models.CharField(max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    doctor = models.CharField(max_length=50, null=True, blank=True)
    address = models.UUIDField(null=True, blank=True)
