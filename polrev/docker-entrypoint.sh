#!/bin/sh

set -e

yarn build
# activate our virtual environment here
#. /opt/pysetup/.venv/bin/activate

python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
gunicorn polrev.wsgi:application

# You can put other setup logic here

# Evaluating passed command:
exec "$@"