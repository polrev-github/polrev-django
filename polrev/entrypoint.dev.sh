python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
#python manage.py runserver 0.0.0.0:8000
gunicorn polrev.wsgi:application