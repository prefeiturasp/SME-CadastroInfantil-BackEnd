from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField

from cadastro_infantil.apps.formulario.models import DadosCrianca


class DadosCriancaCreateSerializer(serializers.ModelSerializer):
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
        if not value:
            raise serializers.ValidationError("Certidão deve ser enviado")
        return value
