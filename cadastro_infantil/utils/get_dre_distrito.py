from cadastro_infantil.apps.dres.models import CepDistritoDRE


def get_dre_distrito(cep):
    try:
        return CepDistritoDRE.objects.values_list('nm_distrito', 'sg_dre').get(cd_cep=cep)
    except CepDistritoDRE.DoesNotExist:
        return "NÃO ENCONTRADO", "NÃO ENCONTRADO"
