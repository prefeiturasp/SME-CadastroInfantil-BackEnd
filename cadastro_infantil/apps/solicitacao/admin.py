from django.contrib import admin

from cadastro_infantil.apps.solicitacao.models import Solicitacao
from cadastro_infantil.utils.excel_utils import export_all

export_all.short_description = 'Exportar todos'


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = (
        'get_nr_solicitacao', 'get_crianca_nome', 'nascimento_crianca', 'endereco_completo', 'cep_moradia', 'dre',
        'distrito', 'exportado')
    list_filter = ('exportado', 'dre')
    list_per_page = 25
    list_editable = ('dre',)
    readonly_fields = ('dados',)
    actions = [export_all, ]
    list_select_related = ['dados', ]

    #######################################################
    def get_crianca_nome(self, obj):
        return obj.dados.nome_crianca

    get_crianca_nome.short_description = 'Nome Criança'

    #######################################################
    def get_nr_solicitacao(self, obj):
        return obj.protocolo

    get_nr_solicitacao.short_description = 'Nro'

    #######################################################

    def changelist_view(self, request, extra_context=None):
        actions = self.get_actions(request)
        if (actions and request.method == 'POST' and 'index' in request.POST and
                request.POST['action'].startswith('export_all')):
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
