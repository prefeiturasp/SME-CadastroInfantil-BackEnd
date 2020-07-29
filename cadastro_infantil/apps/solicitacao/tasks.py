from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from config import celery_app


@celery_app.task(name='envia_confirmacao_cadastro', autoretry_for=(SMTPException,),
                 retry_backoff=2,
                 retry_kwargs={'max_retries': 8}, )
def envia_confirmacao_cadastro(**kwargs):
    para = str(kwargs.get('para')).lower()
    protocolo = kwargs.get('protocolo')
    assunto = f"Confirmação de cadastro"
    txt_msg = f"Recebemos seu cadastro sob número de protocolo {protocolo}."

    html_msg = render_to_string('solicitacao/confirmacao_cadastro.html', kwargs)
    send_mail(assunto, message=txt_msg, html_message=html_msg, recipient_list=[para],
              from_email=settings.DEFAULT_FROM_EMAIL)
    return {'status': True}
