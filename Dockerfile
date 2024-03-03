###########
# BUILDER #
###########
FROM python:3.11.5-slim as builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

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

WORKDIR /home/appuser/app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY . /home/appuser/app

RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser && \
    chown -R appuser:appgroup /home/appuser/app

USER appuser

RUN chmod +x /home/appuser/app/entrypoint.sh

CMD ["./entrypoint.sh"]
