from django.db import models

from cadastro_infantil.utils.image_compressor import compress


class DadosCrianca(models.Model):
    SEXO = [
        ("F", "FEMININO"),
        ("M", "MASCULINO")
    ]
    TIPO_RESPONSAVEL = [
        ('P', 'PAI'),
        ('M', 'MAE'),
        ('O', 'OUTRO')
    ]
    nome_crianca = models.CharField(max_length=255, help_text="Nome da criança")
    sexo_crianca = models.CharField(max_length=1, help_text="Sexo da criança (M/F)")
    dt_nasc_crianca = models.DateField(help_text="Data de nascimento da criança")
    cep_moradia = models.CharField(max_length=8, help_text="CEP da crianca (00000000)")
    endereco_moradia = models.CharField(max_length=255, help_text="Endereço da criança sem numero")
    numero_moradia = models.CharField(max_length=20, help_text="Numero do endereço")
    complemento_moradia = models.CharField(max_length=20, blank=True, help_text="Complemento do endereço")
    nome_mae = models.CharField(max_length=255, help_text="Nome da mãe da criança")
    nome_pai = models.CharField(max_length=255, blank=True, help_text="Nome do pai da criança")
    tipo_responsavel = models.CharField(max_length=1, help_text="Tipo de responsavel da crianca")
    nome_responsavel = models.CharField(max_length=255, blank=True, help_text="Nome do responsavel da criança")
    cpf_responsavel = models.CharField(max_length=11, help_text="CPF do responsavel")
    dt_nasc_responsavel = models.DateField(help_text="Data de nascimento do responsavel")
    email_responsavel = models.EmailField(help_text="Email do responsavel")
    certidao_crianca = models.ImageField(help_text="Foto da certidão de nascimento em BASE64")

    CAMPOS_PRA_NORMALIZAR = ['nome_crianca', 'sexo_crianca', 'endereco_moradia', 'numero_moradia',
                             'complemento_moradia', 'nome_mae', 'nome_pai', 'tipo_responsavel', 'nome_responsavel',
                             'email_responsavel']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.certidao_crianca = compress(self.certidao_crianca)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'dados_crianca'
