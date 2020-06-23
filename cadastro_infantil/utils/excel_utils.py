import xlsxwriter
from django.conf import settings
from django.http import HttpResponse
from django.utils.timezone import now

from cadastro_infantil.apps.solicitacao.models import Solicitacao, DRE_CHOICE
from cadastro_infantil.utils.define_agrupamento import define_agrupamento


def export_all(*_):
    return gerador_de_exportacao(fname='todos-cadastro_infantil', mode='all')


def export_novos_por_dre(*_):
    return gerador_de_exportacao(fname='cadastro_infantil', mode='dre')


def gerador_de_exportacao(fname, mode):
    time = now().astimezone().isoformat('T', 'minutes')[:-6]
    filename = f"{fname}_{time}.xlsx"
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    cols = Solicitacao.get_colunas_planilha()
    wbook = xlsxwriter.Workbook(response, {'constant_memory': True})
    if mode == 'all':
        cols.append('exportado')
        solicitacoes = Solicitacao.objects.select_related('dados').values(*cols).all().order_by('dados_id')
        escreve_solicitacoes_planilha(cols, solicitacoes, wbook)
        wbook.close()
        # Marca como exportado
        # solicitacoes.update(exportado=True)
    elif mode == 'dre':
        for sg_dre, nm_dre in DRE_CHOICE:
            solicitacoes = Solicitacao.objects.select_related('dados').values(*cols) \
                .filter(exportado=False, dre=sg_dre).order_by('dados_id')
            escreve_solicitacoes_planilha(cols, solicitacoes, wbook, page_name=nm_dre)
            # Marca como exportado
            solicitacoes.update(exportado=True)
        wbook.close()
    return response


def escreve_solicitacoes_planilha(cols, solicitacoes, wbook, page_name=None):
    """
    Função que escreve as solicitações em uma determinada pasta no Excel
    :param cols: as colunas que serão escritas
    :param solicitacoes: as solicitacoes que serao escritas
    :param wbook: Objeto Workbook com a planilha excel
    :param page_name: Nome da pasta dentro do excel
    """
    bold = wbook.add_format({'bold': True})
    date = wbook.add_format({'num_format': 'dd/mm/yy'})
    date_time = wbook.add_format({'num_format': 'dd/mm/yy hh:mm'})
    wsheet = wbook.add_worksheet(page_name)
    wrow = 0
    # Cabeçalho
    for i, col in enumerate(map(lambda x: str.replace(x, "dados__", ""), cols)):
        wsheet.write(wrow, i, col, bold)
    wrow += 1
    # Dados
    for s in solicitacoes:
        col = 0
        for k, v in s.items():
            if k in Solicitacao.get_date_cols():
                wsheet.write(wrow, col, v, date)
            elif k in Solicitacao.get_datetime_cols():
                v = v.astimezone().replace(tzinfo=None)
                wsheet.write(wrow, col, v, date_time)
            elif k == 'dados__certidao_crianca':
                v = settings.MEDIA_URL + v
                wsheet.write(wrow, col, v)
            elif k == 'dados__tipo_responsavel':
                tipo = {'1': 'FILIACAO 1', '2': 'FILIACAO 2', '3': 'OUTRO'}
                wsheet.write(wrow, col, tipo.get(v, v))
            elif k == 'dados__raca_cor_crianca':
                raca = {"1": 'AMARELA', "2": 'BRANCA', "3": 'INDIGENA',
                        "4": 'PARDA', "5": 'PRETA', "6": "NAO DECLARADA"}
                wsheet.write(wrow, col, raca.get(v, v))
            elif k == 'agrupamento':
                v = v if len(v) > 0 else define_agrupamento(s.get('dados__dt_nasc_crianca'))
                wsheet.write(wrow, col, v)
            else:
                wsheet.write(wrow, col, v)
            col += 1
        wrow += 1
