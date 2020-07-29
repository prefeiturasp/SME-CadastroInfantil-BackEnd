from django.db import models


class CepDistritoDRE(models.Model):
    cd_cep = models.CharField(max_length=8, help_text="CEP (00000000)", unique=True)
    nm_distrito = models.CharField(max_length=50, help_text="Nome do Distrito")
    sg_dre = models.CharField(max_length=3, help_text="Sigla da DRE")
    nm_dre = models.CharField(max_length=25, help_text="Nome da DRE")

    class Meta:
        verbose_name = 'DRE'
        verbose_name_plural = "DREs"
        db_table = 'CI_cep_distrito_dre'

    def __str__(self):
        return f"{self.cd_cep} - {self.sg_dre}"
