# Base Python Image
FROM python:3.10.16-slim-bookworm AS python-base

# Expose HTTP Port
EXPOSE 8000

# Environment Variables
ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PORT=8000 \
    # Python optimization
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # uv binary path
    PATH="$PATH:/root/.local/bin"

# Django Base Image
FROM python-base AS django-base

# Install required system packages
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
    && rm -rf /var/lib/apt/lists/*

# Secure `uv` installation
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && uv --version

# Create a dedicated user
RUN useradd --create-home --shell /bin/bash --uid 1000 polrev

# Set up work directory with correct permissions
RUN mkdir -p /app && chown -R polrev:polrev /app

# Copy entrypoint scripts before mounting /app
COPY ./web-entrypoint.sh /web-entrypoint.sh
COPY ./celery-entrypoint.sh /celery-entrypoint.sh

# Set correct permissions for scripts
RUN chmod +x /web-entrypoint.sh
RUN chmod +x /celery-entrypoint.sh

# Copy project files for dependency installation
COPY --chown=polrev:polrev ./pyproject.toml /tmp/

# Set work directory for dependency installation
WORKDIR /tmp

# Install dependencies using `uv`
RUN uv pip install --system .

# Switch to the application directory
WORKDIR /app

# Use non-root user
USER polrev

# Development Stage
FROM django-base AS development

# Django Settings
ENV DJANGO_SETTINGS_MODULE polrev.settings.development

ENTRYPOINT ["/web-entrypoint.sh"]
CMD python ./manage.py runserver 0.0.0.0:8000

# Production Stage
FROM django-base AS production

# Django Settings
ENV DJANGO_SETTINGS_MODULE polrev.settings.production

ENTRYPOINT ["/web-entrypoint.sh"]
CMD gunicorn -c ./gunicorn.conf.py polrev.wsgi:application

