# from datetime import datetime

# from django.conf import settings
from django.contrib.auth import get_user_model
# from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from fe_core.models import Entity, UUIDModel

User = get_user_model()


# class AmputationReason(UUIDModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=50, null=True)
#     enabled = models.BooleanField(default=True)

#     class Meta:
#         ordering = ("name",)


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
    name = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    doctor = models.CharField(max_length=50, null=True, blank=True)
    address = models.UUIDField(null=True, blank=True)
    objects = InstitutionManager()

    class Meta:
        ordering = ("name",)

# class PatientManager(models.Manager):
#     def pesquisar(self, query=None):
#         filtros = Q()
#         if query:
#             filtros = filtros & Q(nome__icontains=query) | Q(cidade__icontains=query)
#             return super(PatientManager, self).get_query_set().filter(filtros)
#         else:
#             return super(PatientManager, self).get_query_set()


# class Patient(UUIDModel):
#     SEXO_MASCULINO = 'M'
#     SEXO_FEMININO = 'F'
#     SEXO_CHOICES = (
#         (SEXO_MASCULINO, 'Masculino'),
#         (SEXO_FEMININO, 'Feminino')
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     transiente = models.BooleanField(default=True)
#     codigo_principal = models.IntegerField(null=True, blank=True)
#     nome = models.CharField(max_length=80, null=True)
#     endereco = models.CharField(max_length=80, null=True, blank=True)
#     bairro = models.CharField(max_length=30, null=True, blank=True)
#     cidade = models.CharField(max_length=30, null=True, blank=True)
#     estado = models.CharField(max_length=2, null=True, blank=True)
#     cep = models.CharField(max_length=10, null=True, blank=True)
#     rg = models.CharField(max_length=15, null=True, blank=True)
#     cpf = models.CharField(max_length=14, null=True, blank=True)
#     data_de_nascimento = models.DateTimeField(null=True, blank=True)
#     profissao = models.CharField(max_length=30, null=True, blank=True)
#     fone1 = models.CharField(max_length=15, null=True, blank=True)
#     fone2 = models.CharField(max_length=15, null=True, blank=True)
#     fone3 = models.CharField(max_length=50, null=True, blank=True)
#     altura = models.CharField(max_length=10, null=True, blank=True)
#     peso = models.CharField(max_length=10, null=True, blank=True)
#     protetizacao = models.CharField(max_length=50, null=True, blank=True)
#     tempo_amputacao = models.CharField(max_length=50, null=True, blank=True)
#     motivo_amputacao = models.CharField(max_length=50, null=True, blank=True)
#     motivo_amputacao2 = models.ForeignKey(AmputationReason, null=True, blank=True)
#     membro_amputado = models.CharField(max_length=40, null=True, blank=True)
#     membro_amputado2 = models.ForeignKey(AmputeeMember, null=True, blank=True)
#     sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)

#     original_data_da_avaliacao = models.DateTimeField(null=True, blank=True)
#     original_idade = models.CharField(max_length=50, null=True, blank=True)
#     original_sexo = models.CharField(max_length=10, null=True, blank=True)
#     original_instituicao = models.CharField(max_length=80, null=True, blank=True)
#     original_observacoes = models.TextField(null=True, blank=True)
#     original_observacoes2 = models.TextField(null=True, blank=True)
#     original_medico = models.CharField(max_length=50, null=True, blank=True)
#     original_hospital = models.CharField(max_length=80, null=True, blank=True)
#     original_data_atendimento = models.DateTimeField(null=True, blank=True)

#     objects = PatientManager()

#     def telefones(self):
#         fones = []
#         if self.fone1:
#             fones.append(self.fone1)
#         if self.fone2:
#             fones.append(self.fone2)
#         if self.fone3:
#             fones.append(self.fone3)
#         return ", ".join(fones)

#     def get_idade(self):
#         return 0
        # if self.data_de_nascimento:
        #     today = datetime.now()
        #     try:
        #         birthday = self.data_de_nascimento.replace(year=today.year)
        #     except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
        #         birthday = self.data_de_nascimento.replace(
        #             year=today.year, day=self.data_de_nascimento.day-1)
        #     retorno = today.year - \
        #         self.data_de_nascimento.year - (birthday > today)
        #     return retorno
        # elif self.original_idade:
        #     return self.original_idade
        # else:
        #     return None


# class ProteseTipo(UUIDModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     codigo_tipo = models.IntegerField(null=True)
#     nome = models.CharField(max_length=50, null=True, blank=True)
#     grupo = models.IntegerField(null=True, blank=True)
#     tipo_de_protese = models.CharField(max_length=50, blank=True, null=True)
#     tipo_abreviado = models.CharField(max_length=30, blank=True, null=True)
#     regioes = models.TextField(u"Regiões", null=True, blank=True)
    # arquivo = models.ForeignKey(Arquivo, null=True)
    # arquivo_mongo = models.OneToOneField(ArquivoMongo, null=True)

    # def admin_imagem(self):
    #     if self.arquivo_mongo:
    #         url = self.arquivo_mongo.link()
    #         url = '<img src="%s" width="150" length="150" />' % url
    #         return url
    #     else:
    #         return None
    # admin_imagem.allow_tags = True
    # admin_imagem.short_description = 'Imagem'

    # def admin_imagem_regioes(self):
    #     if self.arquivo_mongo:
    #         url = self.url_imagem_regioes()
    #         url = '<img src="%s" width="150" length="150" />' % url
    #         return url
    #     else:
    #         return None
    # admin_imagem.allow_tags = True
    # admin_imagem.short_description = 'Imagem Regiões'

    # def admin_imagem_400(self):
    #     if self.arquivo_mongo:
    #         url = self.arquivo_mongo.link()
    #         url = '<img src="%s" width="400" length="400" />' % url
    #         return url
    #     else:
    #         return None
    # admin_imagem_400.allow_tags = True
    # admin_imagem_400.short_description = 'Imagem Cadastrada'

    # def admin_imagem_400_regioes(self):
    #     if self.arquivo_mongo:
    #         url = self.url_imagem_regioes()
    #         url = '<img src="%s" width="400" length="400" />' % url
    #         return url
    #     else:
    #         return None
    # admin_imagem_400_regioes.allow_tags = True
    # admin_imagem_400_regioes.short_description = u'Imagem Cadastrada (Regiões)'

    # def url_imagem_regioes(self):
    #     return reverse('protese_tipo_regioes', args=(self.uuid,))

    # def __unicode__(self):
    #     return "%s # %s" % (self.codigo_tipo, self.tipo_de_protese)

    # class Meta:
    #     verbose_name = u"Tipo de Prótese"
    #     verbose_name_plural = u"Tipos de Próteses"
    #     ordering = ('codigo_tipo',)


# class Situacao(UUIDModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     nome = models.CharField(max_length=20)
#     ativo = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = u'Situação'
#         verbose_name_plural = u'Situações'


class Color(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


# class TipoDeAmputacao(UUIDModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     nome = models.CharField(max_length=50)
#     ativo = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = u'Tipo de Amputação'
#         verbose_name_plural = u'Tipos de Amputações'


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


# class ResponsavelTecnico(UUIDModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     nome = models.CharField(max_length=50)
#     ativo = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = u'Responsável Técnico'
#         verbose_name_plural = u'Responsáveis Técnicos'


# class TipoMolde(UUIDModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     nome = models.CharField(max_length=50)
#     ativo = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = u'Tipo de Molde'
#         verbose_name_plural = u'Tipos de Moldes'


# class Protese(UUIDModel):
#     COMPRIMENTO_DISTAL = 1
#     COMPRIMENTO_PROXIMAL = 2
#     COMPRIMENTO_MEDIO = 3
#     COMPRIMENTO_CHOICES = (
#         (COMPRIMENTO_DISTAL,   '1/3 DISTAL'),
#         (COMPRIMENTO_PROXIMAL, '1/3 PROXIMAL'),
#         (COMPRIMENTO_MEDIO,    '1/3 MÉDIO'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
#     transiente = models.BooleanField(default=True)
#     paciente = models.ForeignKey(Patient)

#     data_da_avaliacao = models.DateTimeField(null=True, blank=True)
#     instituicao = models.ForeignKey(Institution, on_delete=models.PROTECT, null=True, blank=True)
#     codigo_principal = models.IntegerField(null=True, blank=True)
#     codigo_protese = models.CharField(max_length=50, null=True, blank=True)
#     nome_do_paciente = models.CharField(max_length=50, null=True, blank=True)
#     data_molde = models.DateTimeField(null=True, blank=True)
#     data_envio = models.DateTimeField(null=True, blank=True)
#     data_recebimento = models.DateTimeField(null=True, blank=True)
#     data_prova = models.DateTimeField(null=True, blank=True)
#     data_entrega = models.DateTimeField(null=True, blank=True)
#     tipo_de_protese = models.CharField(max_length=50, null=True, blank=True)
#     comprimento_coto = models.CharField(max_length=20, null=True, blank=True)
#     comprimento = models.PositiveIntegerField(choices=COMPRIMENTO_CHOICES, null=True, blank=True)
#     observacoes = models.TextField(null=True, blank=True)
#     data_da_1a_protetizacao = models.CharField(max_length=50, null=True, blank=True)
#     tipo_de_protese_antiga = models.CharField(max_length=50, null=True, blank=True)
#     tempo_de_uso = models.CharField(max_length=20, null=True, blank=True)
#     dificuldades = models.TextField(null=True, blank=True)
#     desenho = models.TextField(null=True, blank=True)
#     a = models.CharField(max_length=50, null=True, blank=True)
#     b = models.CharField(max_length=50, null=True, blank=True)
#     c = models.CharField(max_length=50, null=True, blank=True)
#     d = models.CharField(max_length=50, null=True, blank=True)
#     e = models.CharField(max_length=50, null=True, blank=True)
#     f = models.CharField(max_length=50, null=True, blank=True)
#     g = models.CharField(max_length=50, null=True, blank=True)
#     h = models.CharField(max_length=50, null=True, blank=True)
#     i = models.CharField(max_length=50, null=True, blank=True)
#     j = models.CharField(max_length=50, null=True, blank=True)
#     k = models.CharField(max_length=50, null=True, blank=True)
#     number_5 = models.CharField(max_length=6, null=True, blank=True)
#     number_10 = models.CharField(max_length=6, null=True, blank=True)
#     number_15 = models.CharField(max_length=6, null=True, blank=True)
#     number_20 = models.CharField(max_length=6, null=True, blank=True)
#     number_25 = models.CharField(max_length=6, null=True, blank=True)
#     number_30 = models.CharField(max_length=6, null=True, blank=True)
#     number_35 = models.CharField(max_length=6, null=True, blank=True)
#     number_40 = models.CharField(max_length=6, null=True, blank=True)
#     grupo = models.CharField(max_length=50, null=True, blank=True)
#     bock = models.IntegerField(null=True, blank=True)
#     protese_tipo = models.ForeignKey(ProteseTipo, null=True)
#     situacao = models.ForeignKey(Situacao, null=True, blank=True)
#     cor = models.ForeignKey(Cor, null=True, blank=True)
#     tipo_de_amputacao = models.ForeignKey(TipoDeAmputacao, null=True, blank=True)
#     confeccao = models.ForeignKey(Confeccao, null=True, blank=True)
#     lado = models.ForeignKey(Side, null=True, blank=True)
#     responsavel_tecnico = models.ForeignKey(ResponsavelTecnico, null=True, blank=True)
#     number_1a_protetizacao = models.CharField(max_length=20, null=True, blank=True)
#     primeira = models.BooleanField(default=False, blank=True)
#     materiais = models.BooleanField(default=False, blank=True)
#     tipo_confeccao = models.CharField(max_length=10, null=True, blank=True)
#     tipo_molde = models.ForeignKey(TipoMolde, null=True, blank=True)

#     original_instituicao = models.CharField(max_length=80, null=True, blank=True)
#     original_tipo_de_amputacao = models.CharField(max_length=50, null=True, blank=True)
#     original_responsavel_tecnico = models.CharField(max_length=50, null=True, blank=True)
#     original_confeccao = models.CharField(max_length=30, null=True, blank=True)
#     original_lado = models.CharField(max_length=20, null=True, blank=True)
#     original_cor = models.CharField(max_length=20, null=True, blank=True)
#     original_situacao = models.CharField(max_length=20, null=True, blank=True)
#     original_materiais = models.IntegerField(null=True, blank=True)
#     original_data_atendimento = models.DateTimeField(null=True, blank=True)

    # def link_imagem(self):
    #     if self.protese_tipo and self.protese_tipo.arquivo_mongo:
    #         return self.protese_tipo.arquivo_mongo.link()
    #     else:
    #         url = '%sortopedica/images/imagem_nao_disponivel.jpg' % settings.STATIC_URL
    #         return url

    # def link_imagem_regioes(self):
    #     if self.protese_tipo and self.protese_tipo.arquivo_mongo:
    #         url = reverse('paciente_protese_imagem', args=(
    #             self.uuid, self.protese_tipo.uuid))
    #         return url
    #     else:
    #         url = '%sortopedica/images/imagem_nao_disponivel.jpg' % settings.STATIC_URL
    #         return url

    # def link_imagem_com_medidas(self):
    #     if self.protese_tipo and self.protese_tipo.arquivo_mongo:
    #         url = reverse('paciente_protese_imagem_medidas',
    #                       args=(self.uuid, self.protese_tipo.uuid))
    #         return url
    #     else:
    #         return None
