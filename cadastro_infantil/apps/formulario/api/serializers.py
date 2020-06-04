from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField

from cadastro_infantil.apps.formulario.models import DadosCrianca
from cadastro_infantil.utils.remove_acentos import remover_acentos


class DadosCriancaCreateSerializer(serializers.ModelSerializer):
    sexo_crianca = serializers.ChoiceField(choices=DadosCrianca.SEXO)
    tipo_responsavel = serializers.ChoiceField(choices=DadosCrianca.TIPO_RESPONSAVEL)
    certidao_crianca = HybridImageField(required=True)

    class Meta:
        model = DadosCrianca
        fields = ('nome_crianca',
                  'sexo_crianca',
                  'dt_nasc_crianca',
                  'cep_moradia',
                  'endereco_moradia',
                  'numero_moradia',
                  'complemento_moradia',
                  'nome_mae',
                  'nome_pai',
                  'tipo_responsavel',
                  'nome_responsavel',
                  'cpf_responsavel',
                  'dt_nasc_responsavel',
                  'email_responsavel',
                  'certidao_crianca')

    def validate_certidao_crianca(self, value):
        print('CERTIDAO')
        if not value:
            raise serializers.ValidationError("Certidão deve ser enviado")
        return value

    def validate(self, attrs):
        for campo in DadosCrianca.CAMPOS_PRA_NORMALIZAR:
            attrs[campo] = remover_acentos(str(attrs[campo]).upper())
        return attrs
