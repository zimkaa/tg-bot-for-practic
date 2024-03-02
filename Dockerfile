###########
# BUILDER #
###########
FROM python:3.11.5-slim as builder

ARG ENVIRONMENT

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    ENVIRONMENT=${ENVIRONMENT} \
    POETRY_VERSION=1.6.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# RUN addgroup --system appgroup
# RUN adduser --system --shell /bin/sh --disabled-login --disabled-password --ingroup appgroup appuser

# WORKDIR /home/appuser/app/

# RUN chown -R appuser:appgroup /home/appuser/app

# USER appuser

# RUN python -m venv /home/appuser/app/.venv
# ENV PATH="/home/appuser/app/.venv/bin:$PATH"

# RUN pip install --upgrade pip && pip install "poetry==$POETRY_VERSION"

# COPY poetry.lock pyproject.toml /home/appuser/app/

# RUN poetry install --no-dev --no-interaction --no-ansi --no-root && rm -rf $POETRY_CACHE_DIR

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /app/

RUN pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev && \
    pip install --no-cache-dir --upgrade -r requirements.txt

###########
## IMAGE ##
###########
FROM python:3.11.5-slim

# RUN addgroup --system appgroup
# RUN adduser --system --shell /bin/sh --disabled-login --disabled-password --ingroup appgroup appuser

# USER appuser
# WORKDIR /home/appuser/app

# COPY --chown=appuser:appgroup --from=builder /home/appuser/app/.venv /home/appuser/app/.venv

# ENV PATH="/home/appuser/app/.venv/bin:$PATH"

# COPY --chown=appuser:appgroup ./bot /home/appuser/app/bot/

# COPY --chown=appuser:appgroup ./entrypoint.sh /home/appuser/app/

FROM python:3.11.5-slim

WORKDIR /home/appuser/app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY . /home/appuser/app

RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser && \
    chown -R appuser:appgroup /home/appuser/app

USER appuser

RUN chmod +x /home/appuser/app/entrypoint.sh

CMD ["./entrypoint.sh"]
