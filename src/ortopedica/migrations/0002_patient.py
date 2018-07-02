# Generated by Django 2.0.6 on 2018-06-30 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fe_core', '0001_initial'),
        ('ortopedica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transient', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=80, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('rg', models.CharField(blank=True, max_length=15, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('phone1', models.CharField(blank=True, max_length=15, null=True)),
                ('phone2', models.CharField(blank=True, max_length=15, null=True)),
                ('phone3', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profissao', models.CharField(blank=True, max_length=30, null=True)),
                ('altura', models.CharField(blank=True, max_length=10, null=True)),
                ('peso', models.CharField(blank=True, max_length=10, null=True)),
                ('protetizacao', models.CharField(blank=True, max_length=50, null=True)),
                ('tempo_amputacao', models.CharField(blank=True, max_length=50, null=True)),
                ('amputation_reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ortopedica.AmputationReason')),
                ('amputee_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ortopedica.AmputeeMember')),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fe_core.Entity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
