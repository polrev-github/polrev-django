FROM python:3.10.16-slim-bookworm AS python-base

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  PORT=8000 \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  #PIP_NO_CACHE_DIR=off \
  #PIP_DISABLE_PIP_VERSION_CHECK=on \
  #PIP_DEFAULT_TIMEOUT=100 \
  # uv:
  PATH="$PATH:/root/.local/bin"
  
FROM python-base AS django-base

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
  git \
  curl \
  wget \
  gnupg \
  build-essential \
  libpq-dev \
  libjpeg62-turbo-dev \
  zlib1g-dev \
  libwebp-dev \
  postgresql-client \
  ca-certificates \
  # Installing `uv` package manager:
  && curl -LsSf https://astral.sh/uv/install.sh | sh \
  && uv --version \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /polrev && useradd -d /polrev -u 1000 polrev && chown -R polrev /polrev

COPY --chown=polrev:polrev ./pyproject.toml /tmp/
WORKDIR /tmp

#RUN python -m pip install --upgrade pip setuptools wheel && pip install .
RUN uv pip install --system .

USER polrev

FROM django-base AS development

WORKDIR /app
ENTRYPOINT ["bash", "./web-entrypoint.sh", "$0 $@"]
CMD ["uvicorn", "--reload", "--host=0.0.0.0", "--port=8000", "polrev.wsgi:application"]

FROM django-base AS production

WORKDIR /app
ENTRYPOINT ["bash", "./web-entrypoint.sh", "$0 $@"]
CMD [ "gunicorn", "--worker-class uvicorn.workers.UvicornWorker", "--config ./gunicorn.conf.py", "polrev.wsgi:application"]