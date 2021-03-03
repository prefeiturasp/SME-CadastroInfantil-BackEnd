from django.db import models

from cadastro_infantil.utils.image_compressor import compress


class DadosCrianca(models.Model):
    SEXO = [
        ("F", "FEMININO"),
        ("M", "MASCULINO"),
        ("", "")
    ]
    TIPO_RESPONSAVEL = [
        (1, 'FILIACAO 1'),
        (2, 'FILIACAO 2'),
        (3, 'OUTRO')
    ]
    RACA_COR = [
        (1, 'AMARELA'),
        (2, 'BRANCA'),
        (3, 'INDIGENA'),
        (4, 'PARDA'),
        (5, 'PRETA'),
        (6, 'NAO DECLARADA'),
    ]
    # Crianca
    cpf = models.CharField(max_length=11, help_text="CPF", blank=True, null=True)
    nome_crianca = models.CharField(max_length=255, help_text="Nome da criança")
    sexo_crianca = models.CharField(max_length=1, choices=SEXO, help_text="Sexo da criança (M/F)")
    nacionalidade_crianca = models.CharField(max_length=100, help_text="Nacionalidade da criança")
    dt_entrada_brasil = models.DateField(blank=True, null=True, help_text="Caso estrangeiro, quando entrou no Brasil")
    dt_nasc_crianca = models.DateField(help_text="Data de nascimento da criança")
    uf_nasc_crianca = models.CharField(max_length=20, blank=True, help_text="UF de Nascimento da Criança")
    municipio_nasc_crianca = models.CharField(max_length=100, blank=True,
                                              help_text="Municipio de Nascimento da Criança")
    raca_cor_crianca = models.CharField(max_length=1, choices=RACA_COR)
    tem_nee = models.BooleanField(default=False, help_text="Crianca portadora de Necessidades Especiais?")
    tipo_nee = models.CharField(max_length=255, help_text="Qual necessidade especial", blank=True)

    # Filiacao 1
    filiacao1_nome = models.CharField(max_length=100, help_text="Nome da Filiacao I (Pref. Mãe)")
    filiacao1_falecido = models.BooleanField(default=False, help_text="Filiação I é falecido")
    filiacao1_sexo = models.CharField(max_length=1, choices=SEXO, help_text="Sexo da filiacao I (M/F)")
    filiacao1_nacionalidade = models.CharField(max_length=100, help_text="Nacionalidade da filiacao I")

    # Filiacao 2
    filiacao2_consta = models.BooleanField(default=True, help_text="Filiacao II está na certidão da crianca?")
    filiacao2_nome = models.CharField(max_length=100, help_text="Nome da Filiacao II (Pref. Mãe)", blank=True)
    filiacao2_falecido = models.BooleanField(default=False, help_text="Filiação II é falecido")
    filiacao2_sexo = models.CharField(max_length=1, choices=SEXO, help_text="Sexo da filiacao II (M/F)", blank=True)
    filiacao2_nacionalidade = models.CharField(max_length=100, help_text="Nacionalidade da filiacao II", blank=True)

    # Moradia
    cep_moradia = models.CharField(max_length=8, help_text="CEP da crianca (00000000)")
    endereco_moradia = models.CharField(max_length=255, help_text="Endereço da criança sem numero")
    numero_moradia = models.CharField(max_length=20, help_text="Numero do endereço")
    complemento_moradia = models.CharField(max_length=20, blank=True, help_text="Complemento do endereço")

    # Responsavel
    tipo_responsavel = models.CharField(max_length=1, help_text="Tipo de responsavel da crianca")
    parentesco_responsavel = models.CharField(max_length=50, help_text="Grau de parentesco", blank=True)
    nome_responsavel = models.CharField(max_length=255, blank=True, help_text="Nome do responsavel da criança")
    cpf_responsavel = models.CharField(max_length=11, help_text="CPF do responsavel")
    dt_nasc_responsavel = models.DateField(help_text="Data de nascimento do responsavel")
    email_responsavel = models.EmailField(help_text="Email do responsavel", blank=True)
    telefone_responsavel = models.CharField(max_length=14, help_text="Telefone do responsavel")
    telefone_opcional = models.CharField(max_length=14, help_text="Telefone 2 do responsavel", blank=True)

    # Documento
    certidao_crianca = models.ImageField(help_text="Foto da certidão de nascimento em BASE64")

    # Irmao na rede
    irmao_na_rede = models.CharField(max_length=2, blank=True,
                                     help_text="Criança tem irmao matriculado na rede municipal")
    nome_irmao = models.CharField(max_length=255, blank=True, help_text='Nome do irmão')

    CAMPOS_PRA_NORMALIZAR = ['nome_crianca',
                             'sexo_crianca',
                             'nacionalidade_crianca',
                             'uf_nasc_crianca',
                             'municipio_nasc_crianca',
                             'tipo_nee',
                             'filiacao1_nome',
                             'filiacao1_sexo',
                             'filiacao1_nacionalidade',
                             'filiacao2_nome',
                             'filiacao2_sexo',
                             'filiacao2_nacionalidade',
                             'endereco_moradia',
                             'numero_moradia',
                             'complemento_moradia',
                             'parentesco_responsavel',
                             'nome_responsavel',
                             'email_responsavel',
                             'nome_irmao']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.certidao_crianca = compress(self.certidao_crianca)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'CI_dados_crianca'

    def __str__(self):
        return f"{self.pk} - {self.nome_crianca}"
