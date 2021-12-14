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

## Dump Database

```bash
./manage.py dumpdata --natural-foreign --indent 2 \
    -e contenttypes -e auth.permission  \
    -e wagtailcore.groupcollectionpermission \
    -e wagtailcore.grouppagepermission -e wagtailimages.rendition \
    -e sessions > db.json
```

## Load Database

```bash
./manage.py loaddata db.json
```

## Check Deployment
 DJANGO_SETTINGS_MODULE=polrev.settings.production ./manage.py check --deploy