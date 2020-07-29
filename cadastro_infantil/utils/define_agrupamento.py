from datetime import date, datetime


def define_agrupamento(dt_nascimento):
    ano_atual = datetime.now().year
    faixas = {
        # 'BERCARIO I': date(ano_atual - 1, 4, 1) <= dt_nascimento <= date(ano_atual, 3, 31),
        'BERCARIO I': date(ano_atual - 1, 4, 1) <= dt_nascimento <= datetime.now().date(),
        'BERCARIO II': date(ano_atual - 2, 4, 1) <= dt_nascimento <= date(ano_atual - 1, 3, 31),
        'MINI GRUPO I': date(ano_atual - 3, 4, 1) <= dt_nascimento <= date(ano_atual - 2, 3, 31),
        'MINI GRUPO II': date(ano_atual - 4, 4, 1) <= dt_nascimento <= date(ano_atual - 3, 3, 31),
        'INFANTIL I': date(ano_atual - 5, 4, 1) <= dt_nascimento <= date(ano_atual - 4, 3, 31),
        'INFANTIL II': date(ano_atual - 6, 4, 1) <= dt_nascimento <= date(ano_atual - 5, 3, 31),
    }
    return next((k for k in faixas if faixas[k]), "SEM AGRUPAMENTO")
