from django.contrib import admin

from cadastro_infantil.apps.solicitacao.models import Solicitacao


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = (
        'get_nr_solicitacao', 'get_crianca_nome', 'nascimento_crianca', 'endereco_completo', 'cep_moradia', 'dre',
        'dt_solicitacao', 'exportado')
    list_filter = ('exportado', 'dre')
    list_per_page = 25
    # list_editable = ('dre',)
    readonly_fields = ('dados',)

    list_select_related = ['dados', ]

    def get_crianca_nome(self, obj):
        return obj.dados.nome_crianca

    get_crianca_nome.short_description = 'Nome Criança'

    def get_nr_solicitacao(self, obj):
        return obj.protocolo

    get_nr_solicitacao.short_description = 'Nro'


admin.site.register(Solicitacao, SolicitacaoAdmin)

admin.site.site_header = "Painel de Administração do Cadastro Infantil"
