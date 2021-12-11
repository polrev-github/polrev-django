# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.10.0-slim-buster

# Add user that will be used in the container.
#RUN useradd wagtail

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
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.1.12 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.local/bin"

# Install the project requirements.
#COPY requirements.txt /
#RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
#WORKDIR /app

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
#RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
#COPY --chown=wagtail:wagtail . .

# Copy only requirements, to cache them in docker layer
#COPY --chown=wagtail:wagtail ./poetry.lock ./pyproject.toml /app/

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    curl \
    wget \
    gnupg \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==20.0.4"

RUN mkdir -p /polrev && useradd -d /polrev -u 1000 polrev && chown -R polrev /polrev

COPY --chown=polrev:polrev ./poetry.lock ./pyproject.toml /tmp/
WORKDIR /tmp

#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
#RUN apt-get update && apt-get install -y google-chrome-stable

# Project initialization:
RUN echo "$DJANGO_ENV" && poetry version \
  && poetry install \
    $(if [ "$DJANGO_ENV" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction --no-ansi \
  # Upgrading pip, it is insecure, remove after `pip@21.1`
  && poetry run pip install -U pip \
  # Cleaning poetry installation's cache for production:
  && if [ "$DJANGO_ENV" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi

USER polrev

WORKDIR /app
# Use user "wagtail" to run the build commands below and the server itself.
#USER wagtail

#WORKDIR /polrev

# Collect static files.
#RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
#CMD set -xe; python manage.py migrate --noinput; gunicorn polrev.wsgi:application
ENTRYPOINT ["bash", "./entrypoint.sh"]
