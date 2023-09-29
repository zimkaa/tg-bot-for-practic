FROM python:3.11.5-slim-bookworm as builder

ARG ENVIRONMENT

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VERSION=1.6.1
ENV ENVIRONMENT=${ENVIRONMENT}

RUN addgroup --system appgroup
RUN adduser --system --shell /bin/sh --disabled-login --disabled-password --ingroup appgroup appuser

WORKDIR /home/appuser/app/

RUN chown -R appuser:appgroup /home/appuser/app

USER appuser

RUN python -m venv /home/appuser/app/.venv
ENV PATH="/home/appuser/app/.venv/bin:$PATH"

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /home/appuser/app/

RUN poetry config virtualenvs.create false \
  && poetry install --only=main --no-interaction --no-ansi --no-root


FROM python:3.11.5-slim-bookworm

RUN addgroup --system appgroup
RUN adduser --system --shell /bin/sh --disabled-login --disabled-password --ingroup appgroup appuser

USER appuser
WORKDIR /home/appuser/app

COPY --chown=appuser:appgroup --from=builder /home/appuser/app/.venv /home/appuser/app/.venv

ENV PATH="/home/appuser/app/.venv/bin:$PATH"

COPY --chown=appuser:appgroup ./src /home/appuser/app/

COPY --chown=appuser:appgroup ./entrypoint.sh /home/appuser/app/

EXPOSE 8000

CMD ["./entrypoint.sh"]
