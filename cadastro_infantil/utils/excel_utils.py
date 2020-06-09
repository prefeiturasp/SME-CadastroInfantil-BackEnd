import xlsxwriter
from django.http import HttpResponse
from django.utils.timezone import now
from django.conf import settings

from cadastro_infantil.apps.formulario.models import DadosCrianca
from cadastro_infantil.apps.solicitacao.models import Solicitacao


def export_all(modeladmin, request, queryset):
    time = now().astimezone().isoformat('T', 'minutes')[:-6]
    filename = f"todos-cadastro_infantil_{time}.xlsx"

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    cols = [f"dados__{f.name}" for f in DadosCrianca._meta.get_fields()] + [f.name for f in
                                                                            Solicitacao._meta.get_fields()]
    cols = [col for col in cols if col not in ['id', 'dados__dados', 'dados__id', 'exportado']]
    solicitacoes = Solicitacao.objects.select_related('dados').values(*cols).all()

    wrow = 0
    wbook = xlsxwriter.Workbook(response, {'constant_memory': True, 'in_memory': True})
    bold = wbook.add_format({'bold': True})
    date = wbook.add_format({'num_format': 'dd/mm/yy'})
    date_time = wbook.add_format({'num_format': 'dd/mm/yy hh:mm'})
    wsheet = wbook.add_worksheet()

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
            else:
                wsheet.write(wrow, col, v)
            col += 1
        wrow += 1
    wbook.close()

    # Marca como exportado
    solicitacoes.update(exportado=True)

    return response
