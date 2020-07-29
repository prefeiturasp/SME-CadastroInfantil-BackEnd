from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cadastro_infantil.apps.solicitacao.api.viewsets import CreateSolicitacaoViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("cadastro", CreateSolicitacaoViewSet)


app_name = "api"
urlpatterns = router.urls
