from rest_framework import serializers

from cadastro_infantil.apps.formulario.api.serializers import DadosCriancaCreateSerializer
from cadastro_infantil.apps.solicitacao.models import Solicitacao
from django.utils.timezone import now


class SolicitacaoCreateSerializer(serializers.ModelSerializer):
    dados = DadosCriancaCreateSerializer(required=True, write_only=True, many=False)
    protocolo = serializers.ReadOnlyField(default='protocolo')

    class Meta:
        model = Solicitacao
        fields = ('dados', 'protocolo')
        # read_only_fields = ('protocolo',)

    def create(self, validated_data):
        dados_data = validated_data.pop('dados')
        dados_serializer = self.fields['dados']
        dados = dados_serializer.create(dados_data)
        validated_data['dados_id'] = dados.pk
        validated_data['protocolo'] = f"{now().strftime('%y%m')}{dados.pk}"
        return super().create(validated_data)
