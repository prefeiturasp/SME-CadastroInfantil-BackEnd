from rest_framework import viewsets, mixins, status, views
from rest_framework.decorators import action
from rest_framework.response import Response

from cadastro_infantil.apps.formulario.api.serializers import DadosCriancaCreateSerializer
from cadastro_infantil.apps.formulario.models import DadosCrianca, InativacaoFormulario


class CreateDadosCriancaViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = []
    serializer_class = DadosCriancaCreateSerializer
    queryset = DadosCrianca.objects.all()


class ConsultaCpf(views.APIView):
    def get(self, request, cpf, format=None):
        cpf_existe = DadosCrianca.objects.filter(cpf=cpf).first()
        status_code, mensagem = (status.HTTP_200_OK, "CPF pode ser utilizado!") if not cpf_existe else (status.HTTP_400_BAD_REQUEST, "CPF já foi cadastrado!")
        return Response(f"{mensagem}", status=status_code)


class GetSituacaoSite(views.APIView):
    def get(self, request):
        return Response(InativacaoFormulario.situacao_site(), status=status.HTTP_200_OK)

