FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Instala dependências do sistema
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
 && rm -rf /var/lib/apt/lists/*

# Cria usuário não-root
RUN addgroup --system django \
 && adduser --system --ingroup django django

# Define diretório de trabalho antes (melhora cache)
WORKDIR /app

# Copia apenas requirements
COPY requirements /tmp/requirements

RUN pip install -r /tmp/requirements/production.txt \
 && rm -rf /tmp/requirements

# Copia scripts e já ajusta permissões em uma camada só
COPY ./compose/production/django/entrypoint /entrypoint
COPY ./compose/production/django/start /start
COPY ./compose/production/django/celery/worker/start /start-celeryworker
COPY ./compose/production/django/celery/beat/start /start-celerybeat
COPY ./compose/production/django/celery/flower/start /start-flower

RUN set -eux; \
    for f in /entrypoint /start /start-celeryworker /start-celerybeat /start-flower; do \
        sed -i 's/\r$//g' "$f"; \
        chmod +x "$f"; \
    done; \
    chown django:django /entrypoint /start /start-celeryworker /start-celerybeat /start-flower

# Copia aplicação
COPY --chown=django:django . /app

USER django

ENTRYPOINT ["/entrypoint"]
