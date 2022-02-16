# polrev-django

## Development Setup

### Linux
> .bashrc
```bash
export DOCKER_GATEWAY_HOST="`hostname -I` |awk '{print $1}'  `"
```

## Django Setup

```bash
cd polrev

python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

python manage.py wp2puput polrev.xml --site=https://political-revolution.com

python manage.py runserver

```

## Wagtail Setup

Login to the Wagtail admin:  [http://localhost:8000/admin/](http://localhost:8000/admin/)

Edit the Blog page under Pages.  Change the title to 'Political Revolution'

Navigate to Settings/Sites.  Change the site name to 'Political Revolution'.  Change the root page to 'Political Revolution' as well.

## Docker Compose

### Development

```bash
docker-compose up
```

### Production

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Dump Data

```bash
./manage.py dumpdata --natural-foreign --indent 2 \
    -e contenttypes -e auth.permission  \
    -e wagtailcore.groupcollectionpermission \
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
    -e sessions > ./dump/db.json
```

## Load Data

```bash
./manage.py loaddata ./dump/db.json
```

## Nuke Database
```bash
./manage.py makemigrations puput
./manage.py makemigrations avatar
./manage.py makemigrations
```

## Check Deployment
```bash
DJANGO_SETTINGS_MODULE=polrev.settings.production ./manage.py check --deploy
```

## Traefik/Let's Encrypt
```bash
sudo chmod 600 acme.json
```

## Backup
[https://github.com/prodrigestivill/docker-postgres-backup-local](https://github.com/prodrigestivill/docker-postgres-backup-local)

On the host:

```
sudo mkdir -p /var/opt/polrev/backups && sudo chown -R 999:999 /var/opt/polrev/backups
```

## Generic Production Update Procedure

Might want to do a poetry update before you push.

```
docker-compose down
git pull
docker-compose build web
poetry shell
docker-compose up db
cd polrev
poetry update
./manage.py makemigrations
./manage.py migrate
./manage.py flush --noinput
./manage.py loaddata ./dump/db.json
cd ..
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Postgres
```
psql -U polrev polrev_dev
```