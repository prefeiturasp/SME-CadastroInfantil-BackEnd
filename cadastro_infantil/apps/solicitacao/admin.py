from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter

from cadastro_infantil.apps.solicitacao.models import Solicitacao
from cadastro_infantil.utils.excel_utils import export_all, export_novos_por_dre

export_all.short_description = 'Gerar lista com TODAS as solicitações'
export_novos_por_dre.short_description = 'Exportar novos registros por DRE'


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = (
        'get_nr_solicitacao', 'get_crianca_nome', 'nascimento_crianca', 'endereco_completo',
        'cep_moradia', "get_email_responsavel", 'dre', 'distrito', 'exportado', "finalizado")
    list_filter = (('dt_solicitacao', DateRangeFilter), 'exportado', "finalizado", 'dre',)
    list_per_page = 25
    list_editable = ('dre', "finalizado")
    # list_display_links = None
    exclude = ('dados',)
    readonly_fields = ('crianca_dados',)
    list_select_related = ['dados', ]

    search_fields = ("protocolo", "dados__nome_crianca")

    def exporta_todos(self, request, queryset):
        return export_all(queryset)

    exporta_todos.short_description = 'Gerar lista com TODAS as solicitações'

    actions = [export_novos_por_dre, exporta_todos, ]

    def crianca_dados(self, obj):
        change_url = reverse('admin:formulario_dadoscrianca_change', args=(obj.dados.id,))
        return mark_safe('<a href="%s">%s</a>' % (change_url, obj.dados))

    #######################################################
    def get_crianca_nome(self, obj):
        return obj.dados.nome_crianca

    get_crianca_nome.short_description = 'Nome Criança'

    #######################################################
    def get_nr_solicitacao(self, obj):
        return obj.protocolo

    get_nr_solicitacao.short_description = 'Nro'

    #######################################################

    #######################################################
    def get_email_responsavel(self, obj):
        return str(obj.dados.email_responsavel).lower()

    get_email_responsavel.short_description = 'EMAIL'

    #######################################################

    def changelist_view(self, request, extra_context=None):
        actions = self.get_actions(request)
        if (actions and request.method == 'POST' and 'index' in request.POST and
                (request.POST['action'].startswith('export_all') or
                 request.POST['action'].startswith('export_novos_por_dre'))):
            data = request.POST.copy()
            data['select_across'] = '1'
            request.POST = data
            response = self.response_action(request, queryset=self.get_queryset(request))
            if response:
                return response
        return super().changelist_view(request, extra_context)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Solicitacao, SolicitacaoAdmin)

admin.site.site_header = "Painel de Administração do Cadastro Infantil"
