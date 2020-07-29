from rest_framework import viewsets, mixins

from cadastro_infantil.apps.formulario.api.serializers import DadosCriancaCreateSerializer
from cadastro_infantil.apps.formulario.models import DadosCrianca


class CreateDadosCriancaViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = []
    serializer_class = DadosCriancaCreateSerializer
    queryset = DadosCrianca.objects.all()
