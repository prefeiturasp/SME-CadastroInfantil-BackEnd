from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cadastro_infantil.apps.formulario.api.viewsets import CreateDadosCriancaViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
router.register("test-cadastro", CreateDadosCriancaViewSet)


app_name = "api"
urlpatterns = router.urls
