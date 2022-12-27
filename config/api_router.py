from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cadastro_infantil.apps.solicitacao.api.viewsets import CreateSolicitacaoViewSet
from cadastro_infantil.apps.formulario.api.viewsets import ConsultaCpf, GetSituacaoSite

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("cadastro", CreateSolicitacaoViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path('cpf-existe/<str:cpf>/', ConsultaCpf.as_view()),
    path('situacao-site/', GetSituacaoSite.as_view()),
]
