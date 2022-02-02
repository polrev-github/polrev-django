python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
gunicorn polrev.wsgi:application