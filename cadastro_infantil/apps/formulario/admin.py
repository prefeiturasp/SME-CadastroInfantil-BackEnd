from django.contrib import admin

from cadastro_infantil.apps.formulario.models import DadosCrianca, InativacaoFormulario


#
class DadosCriancaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DadosCrianca._meta.get_fields()]
    readonly_fields = [field.attname for field in DadosCrianca._meta.fields]
    list_per_page = 25
    ordering = ('id',)

    def has_delete_permission(self, request, obj=None):
        pass

    def has_change_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        pass


@admin.register(InativacaoFormulario)
class InativacaoFormularioAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return not InativacaoFormulario.objects.exists()

    list_display = ('id', 'data_inicio', 'data_fim', 'alterado_em')
    readyonly_field = ('alterado_em',)
    fields = ('data_inicio', 'data_fim', 'texto_a_ser_visualizado')


admin.site.register(DadosCrianca, DadosCriancaAdmin)
