from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField

from cadastro_infantil.apps.formulario.models import DadosCrianca
from cadastro_infantil.utils.remove_acentos import remover_acentos


class DadosCriancaCreateSerializer(serializers.ModelSerializer):
    sexo_crianca = serializers.ChoiceField(choices=DadosCrianca.SEXO)
    filiacao1_sexo = serializers.ChoiceField(choices=DadosCrianca.SEXO)
    filiacao2_sexo = serializers.ChoiceField(choices=DadosCrianca.SEXO)
    raca_cor_crianca = serializers.ChoiceField(choices=DadosCrianca.RACA_COR)
    tipo_responsavel = serializers.ChoiceField(choices=DadosCrianca.TIPO_RESPONSAVEL)
    certidao_crianca = HybridImageField(required=True)

    class Meta:
        model = DadosCrianca
        fields = ('nome_crianca',
                  'sexo_crianca',
                  'nacionalidade_crianca',
                  'dt_entrada_brasil',
                  'dt_nasc_crianca',
                  'uf_nasc_crianca',
                  'municipio_nasc_crianca',
                  'raca_cor_crianca',
                  'tem_nee',
                  'tipo_nee',
                  'filiacao1_nome',
                  'filiacao1_falecido',
                  'filiacao1_sexo',
                  'filiacao1_nacionalidade',
                  'filiacao2_consta',
                  'filiacao2_nome',
                  'filiacao2_falecido',
                  'filiacao2_sexo',
                  'filiacao2_nacionalidade',
                  'cep_moradia',
                  'endereco_moradia',
                  'numero_moradia',
                  'complemento_moradia',
                  'tipo_responsavel',
                  'parentesco_responsavel',
                  'nome_responsavel',
                  'cpf_responsavel',
                  'dt_nasc_responsavel',
                  'email_responsavel',
                  'telefone_responsavel',
                  'telefone_opcional',
                  'certidao_crianca',
                  'irmao_na_rede',
                  'nome_irmao'
                  )

    def validate_certidao_crianca(self, value):
        if not value:
            raise serializers.ValidationError("Certidão deve ser enviado")
        return value

    def validate(self, attrs):
        for campo in DadosCrianca.CAMPOS_PRA_NORMALIZAR:
            try:
                attrs[campo] = remover_acentos(str(attrs[campo]).upper())
            except KeyError as e:
                attrs[campo] = ''
        return attrs
