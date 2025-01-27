## Squash Migrations

There was an obsolete dependency on django-colorful that caused migrate to fail.
The solution was to squash the migrations

Example:
```code
python manage.py squashmigrations app_name migration_name
```

What I ran:
```bash
./manage.py squashmigrations puput 0002
```