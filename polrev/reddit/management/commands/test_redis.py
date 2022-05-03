import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

#import redis
from django_redis import get_redis_connection

class Command(BaseCommand):
    help = 'test reddit:redis'

    def handle(self, *args, **options):

        #client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
        client = get_redis_connection("default")

        #client.json().set('reddit:hot', Path.root_path(), hot)
        hot = json.loads(client.get('reddit:hot'))
        print(hot)