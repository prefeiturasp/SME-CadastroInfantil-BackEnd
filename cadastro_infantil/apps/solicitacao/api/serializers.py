from allauth.utils import serialize_instance
from rest_framework import serializers

from cadastro_infantil.apps.formulario.api.serializers import DadosCriancaCreateSerializer
from cadastro_infantil.apps.solicitacao.models import Solicitacao
from cadastro_infantil.apps.solicitacao.tasks import envia_confirmacao_cadastro
from cadastro_infantil.utils.gerador_de_protocolo import gerador_de_protocolo
from cadastro_infantil.utils.get_dre_distrito import get_dre_distrito


class SolicitacaoCreateSerializer(serializers.ModelSerializer):
    dados = DadosCriancaCreateSerializer(required=True, write_only=True, many=False)
    protocolo = serializers.ReadOnlyField(default='protocolo')
    dre = serializers.HiddenField(default='dre')
    distrito = serializers.HiddenField(default='distrito')

    class Meta:
        model = Solicitacao
        fields = ('dados', 'protocolo', 'dre', 'distrito')

    def create(self, validated_data):
        # Extraindo os dados da criança e salvando via serializer
        dados_data = validated_data.pop('dados')
        dados_serializer = self.fields['dados']
        dados = dados_serializer.create(dados_data)

        # Relacionando os dados criados com a solicitacao
        validated_data['dados_id'] = dados.pk

        # Criando o protocolo da solicitacao
        validated_data['protocolo'] = gerador_de_protocolo(dados.pk)

        # Pegando DRE e DISTRITO da solicitacao
        validated_data['distrito'], validated_data['dre'] = get_dre_distrito(dados.cep_moradia)

        # Criando e obtendo a solicitacao
        solicitacao = super().create(validated_data)

        # email
        if solicitacao.protocolo and len(dados.email_responsavel) > 1:
            contexto = {
                'para': dados.email_responsavel,
                'solicitacao': serialize_instance(solicitacao),
                'dados': serialize_instance(dados)
            }
            envia_confirmacao_cadastro.delay(**contexto)
        return solicitacao
