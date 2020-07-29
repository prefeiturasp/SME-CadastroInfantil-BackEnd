from random import randint

from django.utils.timezone import now


def gerador_de_protocolo(pk):
    return f"{now().strftime('%y%m')}{('0000' + str(randint(0000, 9999)))[-4:]}{pk}"
