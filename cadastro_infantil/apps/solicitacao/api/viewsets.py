from rest_framework import viewsets, mixins

from cadastro_infantil.apps.solicitacao.api.serializers import SolicitacaoCreateSerializer
from cadastro_infantil.apps.solicitacao.models import Solicitacao


class CreateSolicitacaoViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = []
    serializer_class = SolicitacaoCreateSerializer
    queryset = Solicitacao.objects.all()
