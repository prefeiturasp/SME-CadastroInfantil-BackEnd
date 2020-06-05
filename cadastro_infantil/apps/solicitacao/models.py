from django.db import models

from cadastro_infantil.apps.formulario.models import DadosCrianca


class Solicitacao(models.Model):
    protocolo = models.CharField(max_length=50, unique=True, help_text="Protocolo automatico")
    dados = models.OneToOneField(DadosCrianca, related_name='dados', on_delete=models.PROTECT)
    exportado = models.BooleanField(default=False, help_text="FLAG que esta solicitacao já foi exportada")
    dre = models.CharField(max_length=50, blank=True, help_text="Seleciona qual DRE é responsavel")
    dt_solicitacao = models.DateTimeField(auto_now_add=True)
    dt_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CI_solicitacao'
