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
    -e sessions -o ./dump/db.json.gz
```

## Load Data

```bash
./manage.py loaddata ./dump/db.json.gz
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

### Development

```
poetry update
./manage.py makemigrations
git push
```

### Production

```
docker-compose down
git pull
docker-compose build web
docker-compose up db
poetry shell
cd polrev
poetry update
./manage.py migrate
./manage.py flush --noinput
./manage.py loaddata ./dump/db.json.gz
cd ..
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Postgres
```
psql -U polrev polrev_dev
```

## [django-dbbackup](https://github.com/jazzband/django-dbbackup)

This is set up to dump to an s3 bucket
Run from inside the django container

```
./manage.py dbbackup -z
```

## [prodrigestivill/postgres-backup-local](https://hub.docker.com/r/prodrigestivill/postgres-backup-local)
### Backup
```
docker run --rm -v "$PWD:/backups" -u "$(id -u):$(id -g)" -e POSTGRES_HOST=db -e POSTGRES_DB=polrev_dev -e POSTGRES_USER=polrev -e POSTGRES_PASSWORD=polrev  prodrigestivill/postgres-backup-local /backup.sh
```

### Restore
```
docker exec --tty --interactive polrev-dbbackup-1 /bin/sh -c "zcat ./backups/daily/polrev_dev-20220317-041422.sql.gz | psql --host db --username=polrev --dbname=polrev_dev -W"
```

## Docker

### Backup
```
docker exec -i polrev-db-1 /usr/bin/pg_dump -U polrev polrev_dev | gzip -9 > 20220418.sql.gz 
```

### SCP
```
scp 20220418.sql.gz me@political-revolution.com:Dev
```

### Restore
```
docker cp 20220418.sql.gz polrev_dbbackup_1:/backups

docker exec --tty --interactive polrev_dbbackup_1 /bin/sh -c "zcat ./backups/20220418.sql.gz | psql --host db --username=polrev --dbname=polrev_dev -W"
 ```

## Delete Wagtail Renditions
```
./manage.py dbshell
polrev_dev=# delete from wagtailimages_rendition;
```

## S3 Synchronization

https://github.com/rclone/rclone/issues/2658

```
rclone sync polrev-backup:polrev-backup minio:polrev-backup --no-gzip-encoding
./manage.py dbrestore -z
#rclone sync polrev:polrev minio:polrev --no-gzip-encoding
rclone sync polrev:polrev/media minio:polrev/media
```
### To Production
```
rclone sync minio:polrev-backup polrev-backup:polrev-backup --no-gzip-encoding
```

## Time Synchronization
 sudo apt install ntpdate
 wsl -d docker-desktop -e "hwclock -s"