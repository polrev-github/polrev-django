import json

from django.core.management.base import BaseCommand

from django_redis import get_redis_connection


class Command(BaseCommand):
    help = "test reddit:redis"

    def handle(self, *args, **options):

        client = get_redis_connection("default")

        hot = json.loads(client.get("reddit:hot"))
        print(hot)
