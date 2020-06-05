from django.core.mail import send_mail

from config import celery_app


@celery_app.task(name='envia_confirmacao_cadastro')
def envia_confirmacao_cadastro(**kwargs):
    para = str(kwargs.get('para')).lower()
    protocolo = kwargs.get('protocolo')
    assunto = f"Confirmação de cadastro"
    send_mail(assunto, message=protocolo, recipient_list=[para], from_email='teste@gmail.com')
    return {'status': True}
