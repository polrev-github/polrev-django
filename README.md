# polrev-django

## Development Setup

### Linux / WSL
> .bashrc
```bash
export DOCKER_GATEWAY_HOST="`hostname -I | awk '{print $1}'`"
export POLREV_DOMAIN=docker.localhost
```

## Django Setup

```bash
cd polrev

python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```

## Wagtail Setup

Login to the Wagtail admin:  [http://localhost:8000/admin/](http://localhost:8000/admin/)

Edit the Blog page under Pages.  Change the title to 'Political Revolution'

Navigate to Settings/Sites.  Change the site name to 'Political Revolution'.  Change the root page to 'Political Revolution' as well.

## Docker Compose

### Development

```bash
cp .env.dev.example .env
cp ./shared/.env.dev.example ./shared/.env
cp docker-compose.dev.yml docker-compose.override.yml
docker compose up
```

### Production

```bash
cp docker-compose.prod.yml docker-compose.override.yml
docker compose up -d
```

## Dump Data

```bash
./manage.py dumpdata --natural-foreign --indent 2 \
    -e contenttypes -e auth.permission  \
    -e wagtailcore.groupcollectionpermission \
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
    -e wagtailsearch.indexentry \
    -e sessions -o ./dump/db.json.gz
```

## Load Data

```bash
cd polrev
./manage.py loaddata ./dump/db.json.gz
```

## Nuke Database
```bash
cd polrev
./manage.py makemigrations puput
./manage.py makemigrations avatar
./manage.py makemigrations
```

## Check Deployment
```bash
cd polrev
DJANGO_SETTINGS_MODULE=polrev.settings.production ./manage.py check --deploy
```

## Traefik/Let's Encrypt
```bash
sudo chmod 600 acme.json
```

## Generic Production Update Procedure

### Development

```bash
cd polrev
hatch shell
./manage.py makemigrations
git push
```

### Production

```bash
docker compose down
git pull
docker compose build
docker compose up db redis
cd polrev
hatch shell
./manage.py migrate
./manage.py flush --noinput
./manage.py loaddata ./dump/db.json.gz --verbosity 3
cd ..
docker compose up -d
```

## Postgres
```bash
psql -U polrev polrev_dev
```

## [django-dbbackup](https://github.com/jazzband/django-dbbackup)

This is set up to dump to an s3 bucket
Run from inside the django container

### Install psql
```bash
sudo apt install postgresql-client
```

### Backup
```bash
./manage.py dbbackup -z
```

### Restore
```bash
./manage.py dbrestore -z
```

## Docker

### Backup
```bash
docker exec -i polrev-db-1 /usr/bin/pg_dump -U polrev polrev_dev | gzip -9 > 20220418.sql.gz 
```

### SCP
```bash
scp 20220418.sql.gz me@pol-rev.com:Dev
```

### Restore
```bash
docker cp 20220418.sql.gz polrev_dbbackup_1:/backups

docker exec --tty --interactive polrev_dbbackup_1 /bin/sh -c "zcat ./backups/20220418.sql.gz | psql --host db --username=polrev --dbname=polrev_dev -W"
 ```

## Delete Wagtail Renditions
```bash
./manage.py dbshell
polrev_dev=# delete from wagtailimages_rendition;
```

## S3 Synchronization

```bash
rclone rcd --rc-web-gui
```

https://github.com/rclone/rclone/issues/2658

### From Production to Development
```bash
cd polrev
rclone sync polrev-backup:polrev-backup minio:polrev-backup --no-gzip-encoding
./manage.py dbrestore -z
rclone sync polrev:polrev/media minio:polrev/media
```

### From Development to Production
```bash
rclone copy minio:polrev-backup polrev-backup:polrev-backup --no-gzip-encoding
```

## Time Synchronization
```bash
sudo apt install ntpdate
wsl -d docker-desktop -e "hwclock -s"
```

## Search
```bash
cd polrev
./manage.py update_index
```