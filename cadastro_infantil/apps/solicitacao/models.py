from django.db import models

from cadastro_infantil.apps.formulario.models import DadosCrianca

DRE_CHOICE = [
    ("BT", "BT - BUTANTA"),
    ("CL", "CL - CAMPO LIMPO"),
    ("CS", "CS - CAPELA DO SOCORRO"),
    ("FB", "FB - FREGUESIA-BRASILANDIA"),
    ("G", "G - GUAIANASES"),
    ("IP", "IP - IPIRANGA"),
    ("IQ", "IQ - ITAQUERA"),
    ("JT", "JT - JACANA-TREMEBE"),
    ("MP", "MP - SAO MIGUEL"),
    ("PE", "PE - PENHA"),
    ("PJ", "PJ - PIRITUBA-JARAGUA"),
    ("SA", "SA - SANTO AMARO"),
    ("SM", "SM - SAO MATEUS"),
    ("NÃO ENCONTRADO", "NÃO ENCONTRADO")
]

class Solicitacao(models.Model):
    protocolo = models.CharField(max_length=50, unique=True, help_text="Protocolo automatico")
    dados = models.OneToOneField(DadosCrianca, related_name='dados', on_delete=models.PROTECT)
    exportado = models.BooleanField(default=False, help_text="FLAG que esta solicitacao já foi exportada")
    dre = models.CharField(max_length=50, blank=True, help_text="Seleciona qual DRE é responsavel", choices=DRE_CHOICE)
    distrito = models.CharField(max_length=50, blank=True, help_text="Seleciona o distrito dessa solicitacao")
    dt_solicitacao = models.DateTimeField(auto_now_add=True)
    dt_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CI_solicitacao'
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    def __str__(self):
        return f'Solicitação nr: {self.protocolo}'

    def nascimento_crianca(self):
        return self.dados.dt_nasc_crianca.strftime('%d/%m/%Y')

    nascimento_crianca.short_description = 'Data Nasc. Criança'

    def cep_moradia(self):
        return f"{self.dados.cep_moradia[0:-3]}-{self.dados.cep_moradia[-3:]}"

    cep_moradia.short_description = 'CEP'

    def endereco_completo(self):
        return f"{self.dados.endereco_moradia}, {self.dados.numero_moradia}, {self.dados.complemento_moradia}"

    @staticmethod
    def get_datetime_cols():
        return ['dt_solicitacao', 'dt_modificacao']

    @staticmethod
    def get_date_cols():
        return ['dados__dt_nasc_crianca', 'dados__dt_entrada_brasil', 'dados__dt_nasc_responsavel', ]
